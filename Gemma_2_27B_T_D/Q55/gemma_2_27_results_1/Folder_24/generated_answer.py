def lists_with_product_equal_n(nums):
    sublists = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if prod(nums[i:j]) == -89:
                sublists.append(nums[i:j])
    return sublists

def prod(lst):
    p = 1
    for x in lst:
        p *= x
    return p