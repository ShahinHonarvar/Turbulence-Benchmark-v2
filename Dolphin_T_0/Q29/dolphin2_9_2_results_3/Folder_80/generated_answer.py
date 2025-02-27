def gcf_two_nums(nums):
    num1 = nums[95]
    num2 = nums[85]
    i = min(num1, num2)
    while i > 0:
        if num1 % i == 0 and num2 % i == 0:
            return i
        i -= 1
    return 1