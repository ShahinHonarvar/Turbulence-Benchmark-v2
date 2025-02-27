import math

def gcf_three_nums(num_list):
    num1 = num_list[20]
    num2 = num_list[51]
    num3 = num_list[62]
    gcf_1_2 = math.gcd(num1, num2)
    return math.gcd(gcf_1_2, num3)