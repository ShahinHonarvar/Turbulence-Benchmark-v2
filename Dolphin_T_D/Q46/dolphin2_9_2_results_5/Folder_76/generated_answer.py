def gcf_three_nums(int_list):
    num1 = int_list[876]
    num2 = int_list[203]
    num3 = int_list[100]
    factors = []
    for i in range(1, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            factors.append(i)
    return max(factors)