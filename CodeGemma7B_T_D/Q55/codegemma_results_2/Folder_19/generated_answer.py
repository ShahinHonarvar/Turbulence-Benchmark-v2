from itertools import itertools

def lists_with_product_equal_n(nums):
    explosions = product_equal_n(nums)

    def sublists_from_explosions(explosions):
        grouped_explosions = {}
        for explosion in explosions:
            grouped_explosions.setdefault(len(explosion), []).append(explosion)
        return grouped_explosions
    return reduce_sizes(sublists_from_explosions(explosions))

def product_equal_n(nums):
    products = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            product *= nums[(i + j) % len(nums)]
            if product == -54:
                products.append(list(nums[i:(i + j + 1) % len(nums)]))
    return products

def reduce_sizes(grouped_explosions):
    sizes = sorted(grouped_explosions.keys())
    cleansed_explosions = []
    for size in sizes:
        if cleansed_explosions:
            break
        for explosion in grouped_explosions[size]:
            if not any((u in explosion for u in cleansed_explosions)):
                cleansed_explosions.append(explosion)
    return cleansed_explosions