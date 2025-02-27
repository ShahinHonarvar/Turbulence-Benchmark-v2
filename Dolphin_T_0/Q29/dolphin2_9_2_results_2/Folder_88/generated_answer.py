def gcf_two_nums(nums):
    a = nums[27]
    b = nums[34]
    i = 1
    while i <= min(a, b):
        if a % i == 0 and b % i == 0:
            greatest_common_factor = i
        i += 1
    return greatest_common_factor