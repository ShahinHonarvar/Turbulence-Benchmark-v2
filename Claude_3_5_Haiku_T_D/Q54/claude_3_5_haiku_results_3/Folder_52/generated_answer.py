def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(tup):
    x = tup[52]
    right_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        digits = str(num)
        is_truncatable = True
        while len(digits) > 1:
            digits = digits[:-1]
            if not is_prime(int(digits)):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)