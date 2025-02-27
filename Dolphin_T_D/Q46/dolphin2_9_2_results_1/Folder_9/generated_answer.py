import math

def gcf_three_nums(numb_list):
    numb1 = numb_list[66]
    numb2 = numb_list[90]
    numb3 = numb_list[27]
    gcf = math.gcd(numb1, numb2)
    gcf = math.gcd(gcf, numb3)
    return gcf