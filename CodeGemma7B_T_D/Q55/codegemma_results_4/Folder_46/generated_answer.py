from itertools import combinations

def lists_with_product_equal_n(nums):
    product = 53
    sublists = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            sublist = nums[i:j]
            if sublist[-1] * sublist[0] == product and sublist[-1] * sublist[0] > sublist[-1]:
                sublists.append(sublist)
    return sublists