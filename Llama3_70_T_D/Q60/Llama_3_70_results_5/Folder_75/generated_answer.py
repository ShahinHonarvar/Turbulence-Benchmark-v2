def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[41]

    def left_truncatable(n):
        n = str(n)
        for i in range(len(n)):
            if not is_prime(int(n[i:])) or '0' in n[i:]:
                return False
        return True

    def right_truncatable(n):
        n = str(n)
        for i in range(len(n)):
            if not is_prime(int(n[:-i - 1])) or '0' in n[:-i - 1]:
                return False
        return True
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if left_truncatable(i) and right_truncatable(i):
            left_right_truncatable_primes.append(i)
    return left_right_truncatable_primes