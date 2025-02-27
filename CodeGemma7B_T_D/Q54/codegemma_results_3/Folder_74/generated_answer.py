from math import sqrt
  from itertools import count

def all_right_truncatable_prime(n):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable_prime(n):
        if not is_prime(n):
            return False
        for i in count(1):
            new_n = n // 10 + i * 10
            if not is_prime(new_n):
                return False
        return True
    Primes = [n for n in range(2, int(n[36])) if is_prime(n)]
    return sorted([p for p in Primes if right_truncatable_prime(p)])