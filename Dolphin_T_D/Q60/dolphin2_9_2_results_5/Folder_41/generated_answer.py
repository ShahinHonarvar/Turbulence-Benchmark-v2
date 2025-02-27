def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[46]
    primes = []
    for num in range(2, x + 1):
        if '0' not in str(num) and all((is_prime(int(str(num)[i:j])) for i in range(len(str(num))) for j in range(i + 2, len(str(num)) + 1))):
            primes.append(num)
    return sorted(primes, reverse=True)