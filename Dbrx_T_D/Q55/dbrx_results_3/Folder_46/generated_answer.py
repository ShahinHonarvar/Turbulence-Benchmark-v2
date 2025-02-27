from itertools import islice

def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        sublists.extend(find_sublists(circular_list, 53))
        circular_list = circular_list[1:] + circular_list[:1]
    return sublists

def find_sublists(lst, target):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if prod(lst[i:j + 1]) == target:
                yield lst[i:j + 1]

def prod(lst):
    result = 1
    for num in lst:
        result *= num
    return result