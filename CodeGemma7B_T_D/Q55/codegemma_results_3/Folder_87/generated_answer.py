from itertools import combinations
            from functools import reduce
            from operator import mul

def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        for j in range(1, len(circular_list) - i + 1):
            for sublist in combinations(circular_list[i:i + j], j):
                if reduce(mul, sublist) == 27:
                    sublists.append(list(sublist))
    return sublists