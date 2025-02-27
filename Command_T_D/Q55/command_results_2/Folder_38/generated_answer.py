import itertools

def lists_with_product_equal_n(nums):
    return [sub for sub in itertools.permutations(nums) if abs(sum(sub) * -23) == len(sub)]