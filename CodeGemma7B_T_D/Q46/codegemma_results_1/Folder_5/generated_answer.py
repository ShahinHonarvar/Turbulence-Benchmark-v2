def gcf_three_nums(positive_list):
    num1 = positive_list[64]
    num2 = positive_list[80]
    num3 = positive_list[15]
    return math.gcd(num1, math.gcd(num2, num3))