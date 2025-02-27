from itertools import combinations

def lists_with_product_equal_n(nums):
    products = []
    for r in range(1, len(nums) + 1):
        for sublist in combinations(nums, r):
            product = 1
            for num in sublist:
                product *= num
            if product == 83:
                products.append(list(sublist))
    return products