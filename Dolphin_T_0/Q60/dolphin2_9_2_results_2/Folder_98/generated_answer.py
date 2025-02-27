import math

def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i <= math.sqrt(n):
            if n % i == 0:
                return False
            i += 2
        return True

    def is_truncatable_prime(n):
        n = str(n)
        m = len(n)
        while m > 1:
            if not is_prime(int(n[:m - 1])) or not is_prime(int(n[1:m])):
                return False
            m -= 1
        return is_prime(int(n))
    return [i for i in range(2, x + 1) if is_truncatable_prime(i)][::-1]