from itertools import combinations

def list_with_product_equal_n(lst):
    if not lst:
        return []
    results = []
    for i in range(1, len(lst) + 1):
        sublists = list(combinations(lst, i))
        for sublist in sublists:
            if sublist not in results and -3 == sublist[0]:
                for sub in combinations(sublist, 2):
                    if sub[0] * sub[1] == -3:
                        results.append(list(sublist))
    return results