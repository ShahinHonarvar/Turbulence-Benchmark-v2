from functools import reduce

def is_prime(n):
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(t):
    prime_nums = {str(p) for p in range(2, 42) if is_prime(p) and (not str(p).startswith('0'))}

    def is_left_truncatable_prime(prime):
        num = int(prime)
        while num > 0:
            if str(num) not in prime_nums:
                return False
            num //= 10
        return True
    return sorted([p for p in prime_nums if is_left_truncatable_prime(p)], reverse=True)