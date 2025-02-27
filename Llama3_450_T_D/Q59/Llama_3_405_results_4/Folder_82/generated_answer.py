def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_truncatable_prime(n):
    num_str = str(n)
    if '0' in num_str:
        return False
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:])):
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[69]
    left_truncatable_primes = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    return sorted(left_truncatable_primes, reverse=True)