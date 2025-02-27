from itertools import accumulate, chain, combinations

def lists_with_product_equal_n(nums):
    n = -46
    sublists = [list(sublist) for i in range(1, len(nums) + 1) for sublist in combinations(nums, i) if n in accumulate(chain(sublist, [sublist[0]]))]
    sublists += [list(sublist) for i in range(len(nums)) for sublist in (nums[i:],) if n in accumulate(sublist, initial=nums[i])]
    return sublists