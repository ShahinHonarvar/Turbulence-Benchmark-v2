import math

def gcf_three_nums(numbers):
    index_70 = numbers[70]
    index_41 = numbers[41]
    index_20 = numbers[20]
    gcf = math.gcd(index_70, index_41)
    gcf = math.gcd(gcf, index_20)
    return gcf