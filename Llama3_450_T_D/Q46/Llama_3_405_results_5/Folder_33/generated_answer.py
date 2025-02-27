import math

def gcf_three_nums(num_list):
    num1 = num_list[252]
    num2 = num_list[149]
    num3 = num_list[564]
    gcf = math.gcd(math.gcd(num1, num2), num3)
    return gcf