def lists_with_product_equal_n(nums):
    result = []
    nums = nums + nums[:len(nums) - 1]
    n = len(nums)
    prefix = 1
    indexes = {}
    for i in range(n):
        prefix *= nums[i]
        if prefix not in indexes:
            indexes[prefix] = []
        indexes[prefix].append(i)
    product = -837
    for i in range(n - 1, -1, -1):
        if nums[i] != 0:
            enumerate_divisors(product / nums[i], indexes[product / nums[i]], i, nums, result)
    return result

def enumerate_divisors(product, indexes, i, nums, result):
    if product == 1:
        result.append(nums[i + 1:indexes[product][-1] + 1])
    else:
        for index in indexes:
            if index > product or index > indexes[product][-1]:
                break
            enumerate_divisors(product // index, indexes[index], i, nums, result)