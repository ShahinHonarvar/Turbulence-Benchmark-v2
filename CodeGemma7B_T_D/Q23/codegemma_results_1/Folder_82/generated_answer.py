from math import sqrt

def find_divisors_in_range(num):
    divisors = []
    for i in range(num):
        if num % i == 0 and i >= 4 and (i <= 6):
            divisors.append(i)
    return divisors