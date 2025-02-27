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

def all_left_truncatable_prime(x):
    primes = [n for n in range(2, x) if is_prime(n)]
    result = []
    for prime in primes:
        str_prime = str(prime)
        if '0' not in str_prime:
            is_truncatable = True
            for i in range(1, len(str_prime)):
                if not is_prime(int(str_prime[i:])):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(prime)
    return sorted(result, reverse=True)