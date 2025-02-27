from itertools import combinations

def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(1, len(circular_list) + 1):
        for comb in combinations(circular_list, i):
            if sorted(comb) not in sublists and functools.reduce(lambda x, y: x * y, comb) == 85 and all(circular_list[-1] * circular_list[0] not in comb or functools.reduce(lambda x, y: x * y, set(comb) - {circular_list[-1], circular_list[0]}) == 85 * 85):
                sublists.append(list(sorted(comb)))
    return sublists