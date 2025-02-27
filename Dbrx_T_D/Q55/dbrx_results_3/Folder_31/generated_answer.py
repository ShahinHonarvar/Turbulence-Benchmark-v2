from itertools import islice

def lists_with_product_equal_n(lst):
    for i in range(len(lst) + 1):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            if product(sublist) == -16:
                yield sublist

def product(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

def circular_lists_with_product_equal_n(lst):
    circular_lst = lst + [lst[0]]
    result = list(lists_with_product_equal_n(circular_lst))
    for i in range(len(circular_lst) - 1):
        circular_lst.append(circular_lst.pop(0))
        result.extend(list(lists_with_product_equal_n(circular_lst)))
    return result