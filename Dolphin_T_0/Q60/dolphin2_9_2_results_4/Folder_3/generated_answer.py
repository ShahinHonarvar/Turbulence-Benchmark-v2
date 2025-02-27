def is_prime(n):
    if n in (2, 3):
        return True
    if n in (0, 1) or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[100]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    left_right_truncatable_primes = [i for i in primes if all((is_prime(int(str(i)[j:len(str(i)) - j])) for j in range(1, len(str(i)) // 2)))]
    return sorted(left_right_truncatable_primes)