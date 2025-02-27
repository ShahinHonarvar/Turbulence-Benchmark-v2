def gcf_two_nums(nums):
    num1 = nums[48]
    num2 = nums[76]
    for i in range(min(num1, num2), 1, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i