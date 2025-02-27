from math import sqrt

def find_divisors_in_range(num):
    divisors = []
    for x in range(7, int(sqrt(num)) + 1):
        if num % x == 0:
            divisors.append(x)
            if num // x != x:
                divisors.append(num // x)
    return divisors