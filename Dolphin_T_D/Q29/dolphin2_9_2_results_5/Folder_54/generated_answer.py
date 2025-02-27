def gcf_two_nums(nums):
    num1 = nums[56]
    num2 = nums[92]
    i = min(num1, num2)
    while i > 1:
        if num1 % i == 0 and num2 % i == 0:
            return i
        i -= 1
    return 1