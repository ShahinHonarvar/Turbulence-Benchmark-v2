def gcf_three_nums(nums_list):
    num1 = nums_list[99]
    num2 = nums_list[63]
    num3 = nums_list[74]
    factors = []
    for i in range(1, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            factors.append(i)
    return max(factors)