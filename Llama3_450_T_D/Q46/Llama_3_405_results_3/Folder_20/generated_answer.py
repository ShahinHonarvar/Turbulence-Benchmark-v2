import math

def gcf_three_nums(num_list):
    num1 = num_list[29]
    num2 = num_list[53]
    num3 = num_list[42]
    gcf = math.gcd(math.gcd(num1, num2), num3)
    return gcf