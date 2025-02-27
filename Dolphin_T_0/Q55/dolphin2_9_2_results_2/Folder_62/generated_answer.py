import math

def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= nums[j % n]
            if product % 100 == 0:
                temp = [nums[j % n]]
                k = 1
                while j + k < i + n and k <= i + n - j:
                    k += 1
                    temp.append(nums[(j + k) % n])
                    if math.prod(temp) == 100:
                        result.append(temp)
    return result