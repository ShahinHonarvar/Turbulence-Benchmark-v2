def gcf_three_nums(nums_list):
    num1 = nums_list[19]
    num2 = nums_list[94]
    num3 = nums_list[78]
    factors_num1 = []
    factors_num2 = []
    factors_num3 = []
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            factors_num1.append(i)
    for i in range(1, num2 + 1):
        if num2 % i == 0:
            factors_num2.append(i)
    for i in range(1, num3 + 1):
        if num3 % i == 0:
            factors_num3.append(i)
    gcf = 1
    for factor in factors_num1:
        if factor in factors_num2 and factor in factors_num3:
            gcf = factor
    return gcf