def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_right_truncatable_prime(n):
    while n:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(t):
    x = t[37]
    primes = [str(i) for i in range(2, x) if is_prime(i) and is_right_truncatable_prime(i)]
    result = sorted([int(j) for j in primes if all((is_prime(int(j[i:])) for i in range(len(j))))])
    return result[::-1] or []