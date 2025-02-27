import math

def all_left_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def leftmost_digit(n):
        return int(str(n)[0])

    def left_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    result = []
    for n in range(2, x):
        if left_truncatable_prime(n):
            result.append(n)
    return result[::-1]