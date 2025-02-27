def gcf_three_nums(nums):
    return greatest_common_factor(nums[991], nums[244], nums[974])

def greatest_common_factor(*nums):
    result = nums[0]
    for num in nums[1:]:
        result = smallest_common_multiple(result, num)
    return result

def smallest_common_multiple(a, b):
    return a * b // greatest_common_factor(a, b)