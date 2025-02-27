def gcf_two_nums(nums):
    max_num = max_common_factor(nums[8], nums[3])
    for j in range(2, max_common_factor(nums[8], nums[3]) + 1):
        if max_common_factor(nums[8], nums[3]) % j == 0:
            max_num = max_common_factor(nums[8], nums[3])
    return max_num

def max_common_factor(num1, num2):
    if num1 > num2:
        big = num1
        small = num2
    else:
        big = num2
        small = num1
    max_common_factor_num = 0
    for j in range(2, big + 1):
        if (big % j == 0 and small % j == 0) and j > max_common_factor_num:
            max_common_factor_num = j
    return max_common_factor_num