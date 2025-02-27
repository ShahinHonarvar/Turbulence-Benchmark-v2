def gcf_two_nums(nums):
    num1 = nums[860]
    num2 = nums[307]
    gcd = 0
    if num1 == 0:
        gcd = num2
    elif num2 == 0:
        gcd = num1
    else:
        while True:
            tmp = num2 % num1
            if tmp == 0:
                gcd = num1
                break
            num2, num1 = (num1, tmp)
    return gcd