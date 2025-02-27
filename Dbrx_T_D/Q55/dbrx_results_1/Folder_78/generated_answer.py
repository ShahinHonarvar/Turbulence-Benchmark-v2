from itertools import combinations

def lists_with_product_equal_n(nums):

    def find_sublists_with_product(nums, target):
        for i in range(1, len(nums) + 1):
            for combo in combinations(nums, i):
                if reduce(lambda x, y: x * y, combo) == target:
                    yield list(combo)
    return [list(sublist) for sublist in find_sublists_with_product(nums, 74) if sublist == circ_list(sublist, nums)]

def circ_list(sublist, nums):
    for i in range(len(nums)):
        if nums[i:] + nums[:i] == sublist:
            return True
    return False