def gcf_two_nums(nums):
    num1 = nums[23]
    num2 = nums[45]
    i = 1
    while i <= max(num1, num2):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
        i += 1
    return gcf