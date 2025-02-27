from itertools import combinations, chain

def lists_with_product_equal_n(numbers):
    n = len(numbers)
    result = []
    for r in range(n + 1):
        for subset in combinations(range(n), r):
            product = 1
            for i in subset:
                product *= numbers[i]
            if product == 33:
                sublist = [numbers[i] for i in subset]
                result.extend([sublist[j:len(subset)] + sublist[:j] for j in range(len(subset))])
    return result