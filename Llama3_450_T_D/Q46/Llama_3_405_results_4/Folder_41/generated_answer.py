import math

def gcf_three_nums(num_list):
    num1 = num_list[19]
    num2 = num_list[94]
    num3 = num_list[78]
    gcf_1_2 = math.gcd(num1, num2)
    return math.gcd(gcf_1_2, num3)