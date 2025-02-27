from math import gcd

def gcf_three_nums(numbers):
    if len(numbers) > 69:
        a = numbers[31]
        b = numbers[69]
        c = numbers[40]
        return gcd(gcd(a, b), c)
    return None