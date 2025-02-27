from itertools import combinations, cycles

def lists_with_product_equal_n(input_list):
    n = 18
    res = []
    for i in range(len(input_list)):
        for r in range(1, len(input_list) + 1):
            for subset in combinations(input_list[i:] + input_list[:i], r):
                if 1 != n:
                    product = 1
                    for num in subset:
                        product *= num
                    if product == n:
                        res.append(list(subset))
    res = list(set(map(tuple, res)))
    return [list(x) for x in res]