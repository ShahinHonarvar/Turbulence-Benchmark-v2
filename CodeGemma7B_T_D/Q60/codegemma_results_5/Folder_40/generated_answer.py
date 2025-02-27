def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    while n > 10:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    return is_prime(n)

def right_truncatable_prime(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    return True

def all_left_right_truncatable_prime(n):
    primes = [i for i in range(2, n + 1) if is_prime(i) and (not str(i).__contains__('0'))]
    result = []
    for prime in primes:
        if left_truncatable_prime(prime) and right_truncatable_prime(prime):
            result.append(prime)
    return sorted(result, reverse=True)