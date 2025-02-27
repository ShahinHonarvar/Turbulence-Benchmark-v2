from itertools import combinations

def lists_with_product_equal_n(nums):
    n = 632
    size = len(nums)
    nums += nums
    sublists = []
    for i in range(size):
        for j in range(i + 1, i + size):
            sublist = nums[i:j]
            product = 1
            for num in sublist:
                product *= num
                if product > n:
                    break
            if product == n:
                sublists.append(sublist)
    return sublists