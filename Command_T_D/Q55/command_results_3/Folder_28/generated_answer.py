import itertools

def lists_with_product_equal_n(nums):
    if not 85 in map(lambda x: x * x, nums):
        return []
    sublists = [sub for n, sub in itertools.permutations(nums) if n * n == 85]
    return [sub for sub in sublists if all((x == 85 for x in zip(sub, sub[1:])))]