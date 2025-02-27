import math

def gcf_three_nums(num_list):
    num1 = num_list[818]
    num2 = num_list[606]
    num3 = num_list[873]
    gcf_12 = math.gcd(num1, num2)
    return math.gcd(gcf_12, num3)