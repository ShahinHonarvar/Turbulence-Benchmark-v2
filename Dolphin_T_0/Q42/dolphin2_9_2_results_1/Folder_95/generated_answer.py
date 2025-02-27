def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_factors(num_list):
    num = num_list[87]
    prime_factors_set = set()
    for i in range(1, num + 1):
        if num % i == 0 and is_prime(i):
            prime_factors_set.add(i)
    return prime_factors_set