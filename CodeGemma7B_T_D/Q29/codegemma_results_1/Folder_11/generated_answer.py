def gcf_two_nums(num_list):
    num1 = num_list[64]
    num2 = num_list[80]
    gcd = 1
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
    return gcd