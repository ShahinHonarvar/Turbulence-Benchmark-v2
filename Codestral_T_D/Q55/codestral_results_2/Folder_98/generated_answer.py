from itertools import cycle, islice

def lists_with_product_equal_n(nums):
    n = len(nums)
    nums = nums + nums
    result = []
    for i in range(n):
        for j in range(i + 1, i + n):
            product = 1
            for k in islice(cycle(nums), i, j):
                product *= k
            if product == -1:
                result.append(nums[i:j])
    return result