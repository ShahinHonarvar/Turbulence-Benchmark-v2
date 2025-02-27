def getcf_two_nums(nums):
    num1, num2 = (nums[76], nums[57])
    cf = 1
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            cf = i
    return cf