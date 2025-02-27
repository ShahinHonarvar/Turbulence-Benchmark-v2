def gcf_two_nums(pos_list):
    num1, num2 = (pos_list[380], pos_list[327])
    gcd = 1
    for i in range(2, min(num1, num2) + 1):
        while num1 % i == 0 and num2 % i == 0:
            gcd *= i
            num1 //= i
            num2 //= i
    return gcd