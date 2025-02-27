from primestable import is_prime

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[41]
    l_truncatable_primes = []
    for num in range(1, x):
        if is_left_truncatable_prime(num):
            l_truncatable_primes.append(num)
    return sorted(l_truncatable_primes)

def is_left_truncatable_prime(num):
    if '0' in str(num):
        return False
    while num > 0:
        if not is_prime(num):
            return False
        num = num // 10
    return True