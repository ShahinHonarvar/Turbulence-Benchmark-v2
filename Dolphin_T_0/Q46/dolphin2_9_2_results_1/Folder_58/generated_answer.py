def gcf_three_nums(int_list):
    num1 = int_list[145]
    num2 = int_list[183]
    num3 = int_list[770]
    factors = []
    for i in range(1, num1 + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            factors.append(i)
    return max(factors)