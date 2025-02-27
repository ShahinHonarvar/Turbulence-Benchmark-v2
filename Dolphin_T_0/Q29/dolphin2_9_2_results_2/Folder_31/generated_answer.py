def gcf_two_nums(nums):
    num1 = nums[87]
    num2 = nums[95]
    if num1 > num2:
        for i in range(num2, 0, -1):
            if num1 % i == 0 and num2 % i == 0:
                return i
    else:
        for i in range(num1, 0, -1):
            if num1 % i == 0 and num2 % i == 0:
                return i