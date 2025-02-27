def gcf_three_nums(num_list):
    num1 = num_list[307]
    num2 = num_list[920]
    num3 = num_list[463]
    gcd = 1
    for i in range(2, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
    for i in range(2, min(gcd, num3) + 1):
        if gcd % i == 0 and num3 % i == 0:
            gcd = i
    return gcd