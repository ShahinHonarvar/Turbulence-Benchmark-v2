def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    if str(n)[-1] == '0':
        return False
    for i in range(len(str(n)), 1, -1):
        left = int(str(n)[1:i])
        right = int(str(n)[-i + 1:])
        if not is_prime(left) or not is_prime(right):
            return False
    return True

def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(x * 2, 0, -1):
        if is_truncatable(i):
            primes.append(i)
    return primes