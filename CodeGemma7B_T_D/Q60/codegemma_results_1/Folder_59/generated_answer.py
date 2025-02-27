import math
            import re

def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if not re.search('[0]', str(n)) and is_prime(n):
            for i in range(1, len(str(n))):
                if not is_prime(int(str(n)[:-i])):
                    return False
                if not is_prime(int(str(n)[i:])):
                    return False
            return True
        return False
    left_right_truncatable_primes = []
    for num in x:
        if num <= 100:
            continue
        if is_left_right_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes or []