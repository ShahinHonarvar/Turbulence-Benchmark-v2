def gcf_two_nums(nums):
    num1 = nums[793]
    num2 = nums[449]
    a = min(num1, num2)
    while a > 0:
        if num1 % a == 0 and num2 % a == 0:
            return a
        a -= 1