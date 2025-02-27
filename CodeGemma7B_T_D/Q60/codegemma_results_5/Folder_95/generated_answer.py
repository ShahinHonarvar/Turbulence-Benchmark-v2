import math

def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def left_truncatable(n):
        if n % 2 == 0 or n % 3 == 0:
            return False
        if n < 10:
            return False
        while n >= 10:
            n //= 10
            if not is_prime(n):
                return False
        return True

    def right_truncatable(n):
        if n % 2 == 0 or n % 3 == 0:
            return False
        if n < 10:
            return False
        while n > 9:
            n %= 10 ** int(math.log10(n))
            if not is_prime(n):
                return False
        return True
    result = []
    for n in range(2, x + 1):
        if is_prime(n) and left_truncatable(n) and right_truncatable(n):
            result.append(n)
    return sorted(result)