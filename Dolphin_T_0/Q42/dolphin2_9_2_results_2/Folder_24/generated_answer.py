def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_factors(integer_list):
    number = integer_list[74]
    prime_factors_set = set()
    for i in range(1, number + 1):
        if number % i == 0 and is_prime(i):
            prime_factors_set.add(i)
    return prime_factors_set