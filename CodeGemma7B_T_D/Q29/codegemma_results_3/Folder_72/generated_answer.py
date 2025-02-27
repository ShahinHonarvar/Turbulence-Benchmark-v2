def gcf_two_nums(nums):
    num1 = nums[18]
    num2 = nums[37]
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    elif num1 == num2:
        return num1
    else:
        smaller = min(num1, num2)
        for i in range(smaller, -1, -1):
            if num1 % i == 0 and num2 % i == 0:
                return i