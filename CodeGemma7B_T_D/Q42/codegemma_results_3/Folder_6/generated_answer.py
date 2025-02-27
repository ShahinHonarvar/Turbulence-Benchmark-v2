from math import sqrt

def prime_factors(list):
    prime_factors = set()
    for num in list:
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                prime_factors.add(i)
                while num % i == 0:
                    num //= i
    return prime_factors