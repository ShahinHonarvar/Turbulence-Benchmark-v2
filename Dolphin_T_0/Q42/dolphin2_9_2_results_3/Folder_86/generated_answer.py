def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(int_list):
    num = int_list[194]
    prime_factors_set = set()
    for i in range(2, num + 1):
        if i == 1 or num % i != 0:
            continue
        if is_prime(i):
            prime_factors_set.add(i)
    return prime_factors_set