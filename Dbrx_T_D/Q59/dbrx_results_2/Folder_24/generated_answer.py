def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_leftmost_digit(n):
    return int(str(n)[1:])

def all_left_truncatable_prime(t):
    x = t[65]
    primes = [i for i in range(1, x) if is_prime(i)]
    result = []
    for prime in primes:
        num = prime
        while num > 0:
            if not is_prime(num):
                break
            num = remove_leftmost_digit(num)
        if num == 0:
            result.append(prime)
    return sorted(result, reverse=True)