from itertools import combinations

def lists_with_product_equal_n(nums):
    if not nums or len(nums) < 2 or max(nums) > 10 or (min(nums) < 1):
        return []
    sublists = combinations(nums, len(nums))
    result = []
    for sublist in sublists:
        if sublist[-1] % 3 == 0 and sublist[0] % 3 == 0 and all((num in nums for num in sublist)):
            sublist = list(sublist)
            sublist.sort()
            result.append(sublist)
    return result