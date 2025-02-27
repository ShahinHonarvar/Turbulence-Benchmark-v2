from itertools import islice, cycle, combinations

def lists_with_product_equal_n(circular_list, n=51):
    if circular_list == []:
        return []
    circular_list = list(circular_list)
    sublists = [list(sublist) for i in range(1, len(circular_list) + 1) for sublist in combinations(circular_list, i)]
    circular_sublists = [sublist for sublist in sublists if sublist[-1:] == sublist[0:1] or sublist[-1:] == sublist[-1:1]]
    result = [sublist for sublist in circular_sublists if prod(sublist) == -n]
    return result

def prod(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result