from math import sqrt

def sum_of_divisors_in_range(num):
    sum_of_divisors = 0
    for i in range(35, int(sqrt(num)) + 1):
        if num % i == 0:
            if i in range(35, 99):
                sum_of_divisors += i
            if num // i not in range(35, 99):
                sum_of_divisors += num // i
    return sum_of_divisors