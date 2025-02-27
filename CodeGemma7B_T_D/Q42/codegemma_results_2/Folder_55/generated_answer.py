from math import sqrt

def prime_factors(num_list):
    prime_factors_set = set()
    num = num_list[21]
    for i in range(2, int(sqrt(num)) + 1):
        while num % i == 0:
            prime_factors_set.add(i)
            num //= i
    if num > 1:
        prime_factors_set.add(num)
    return prime_factors_set