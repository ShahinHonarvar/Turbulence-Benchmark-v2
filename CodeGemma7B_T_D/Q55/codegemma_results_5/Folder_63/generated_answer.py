from itertools import combinations

def lists_with_product_equal_n(nums):
    nums.append(nums[0])
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            product = 1
            temp = []
            for k in range(i, j):
                product *= nums[k]
                temp.append(nums[k])
            if product == 96 and len(temp) <= len(nums):
                sublists.append(temp)
    return sublists