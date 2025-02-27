import math

def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sq = int(math.sqrt(n)) + 1
        for divisor in range(3, sq, 2):
            if n % divisor == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        else:
            return is_prime(n) and is_right_truncatable_prime(int(str(n)[:-1]))
    x = t[618]
    return sorted(list(filter(is_right_truncatable_prime, range(1, x))))