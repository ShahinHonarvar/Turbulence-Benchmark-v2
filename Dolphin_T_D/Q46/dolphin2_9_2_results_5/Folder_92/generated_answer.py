def gcf_three_nums(num_list):
    num1 = num_list[7]
    num2 = num_list[9]
    num3 = num_list[0]
    factors = set()
    for i in range(1, max(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            factors.add(i)
    return max(factors)