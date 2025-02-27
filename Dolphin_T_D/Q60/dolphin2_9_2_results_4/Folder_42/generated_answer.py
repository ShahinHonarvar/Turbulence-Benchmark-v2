def is_prime(n):
    if n > 3 and n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    left_right_truncatable_primes = []
    for i in range(x, 1, -1):
        if all((is_prime(int(str(i)[j:i - j])) for j in range(len(str(i)) - 1))):
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes, reverse=True)