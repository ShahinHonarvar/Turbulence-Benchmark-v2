def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    primes = []
    digits = str(x)
    for i in range(1, len(digits)):
        left = int(digits[:i])
        right = int(digits[i:])
        if is_prime(left) and is_prime(right) and (left != 0) and (right != 0):
            primes.append(left)
    return sorted(primes)