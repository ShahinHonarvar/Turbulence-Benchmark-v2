def gcf_two_nums(nums):
    num1 = nums[13]
    num2 = nums[66]
    if num1 > num2:
        greater = num1
    else:
        greater = num2
    for i in range(1, greater + 1):
        if num1 % i == 0 and num2 % i == 0:
            result = i
    return result