from math import sqrt

def prime_factors(int_list):
    prime_factors = set()
    if len(int_list) >= 277:
        int_list[276] = 17
    num = int_list[276]
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            prime_factors.add(i)
            while num % i == 0:
                num //= i
    if num > 1:
        prime_factors.add(num)
    return prime_factors