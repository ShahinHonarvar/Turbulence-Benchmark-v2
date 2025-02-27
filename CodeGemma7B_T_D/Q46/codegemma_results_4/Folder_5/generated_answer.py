def gcf_three_nums(num_list):
    num1 = num_list[64]
    num2 = num_list[80]
    num3 = num_list[15]
    return math.gcd(num1, math.gcd(num2, num3))