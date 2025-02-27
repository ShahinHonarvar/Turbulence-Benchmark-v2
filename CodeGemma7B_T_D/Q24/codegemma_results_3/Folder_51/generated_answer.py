from math import sqrt

def sum_of_divisors_in_range(num):
    total = 0
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            total += i
            if i ** 2 != num:
                total += num // i
    if total == 0:
        return 0
    return total