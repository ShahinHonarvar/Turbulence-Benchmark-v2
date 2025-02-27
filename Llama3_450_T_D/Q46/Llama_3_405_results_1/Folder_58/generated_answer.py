import math

def gcf_three_nums(num_list):
    num1 = num_list[145]
    num2 = num_list[183]
    num3 = num_list[770]
    return math.gcd(math.gcd(num1, num2), num3)