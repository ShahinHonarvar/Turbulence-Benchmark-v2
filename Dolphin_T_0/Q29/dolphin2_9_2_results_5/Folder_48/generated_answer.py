def gcf_two_nums(nums):
    num1 = nums[618]
    num2 = nums[195]
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0:
            greatest_common_factor = i
    return greatest_common_factor