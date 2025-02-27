from itertools import combinations

def lists_with_product_equal_n(nums):
    n = len(nums)
    sublists = []
    for i in range(1, n + 1):
        for subset in combinations(nums, i):
            if i == 1:
                sublists.append([subset[0]])
            else:
                product = 1
                for number in subset:
                    product *= number
                if product == -779:
                    sublists.append(list(subset))
    return sublists