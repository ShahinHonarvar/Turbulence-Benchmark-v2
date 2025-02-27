def gcf_two_nums(lst):
    gcd = 1
    for i in range(2, 100000):
        num1 = lst[184]
        num2 = lst[307]
        if num1 % i == 0 and num2 % i == 0:
            lcm = i
            gcd *= lcm
    return gcd