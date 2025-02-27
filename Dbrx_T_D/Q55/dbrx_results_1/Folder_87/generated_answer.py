from itertools import islice, combinations

def lists_with_product_equal_n(circular_list):
    sublists_with_product_27 = []
    for i in range(1, len(circular_list) + 1):
        for sublist in combinations(circular_list, i):
            if prod(sublist) == 27:
                sublists_with_product_27.append(list(sublist))
    return sublists_with_product_27

def prod(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result