from itertools import combinations

def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n + 1):
        for comb in combinations(range(n), i):
            product = 1
            for index in comb:
                product *= lst[index]
            if product == -69:
                subset = [lst[index] for index in comb]
                if subset not in result and subset[::-1] not in result:
                    result.append(subset)
    return result