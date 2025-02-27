from itertools import islice, cycle

def circular_list_slice(lst, size):
    circular_lst = list(islice(cycle(lst), size))
    return circular_lst

def lists_with_product_equal_n(lst, n):
    result = []
    for i in range(1, len(lst) + 1):
        for j in range(len(lst) - i + 1):
            sublist = lst[j:j + i]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result