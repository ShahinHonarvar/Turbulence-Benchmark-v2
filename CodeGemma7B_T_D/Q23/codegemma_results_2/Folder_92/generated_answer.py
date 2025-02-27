from math import sqrt

def find_divisors_in_range(num):
    divisor_list_in_range = []
    for i in range(8, int(sqrt(num)) + 1):
        if num % i == 0:
            divisor_list_in_range.append(i)
            divisor_list_in_range.append(num // i)
    return divisor_list_in_range