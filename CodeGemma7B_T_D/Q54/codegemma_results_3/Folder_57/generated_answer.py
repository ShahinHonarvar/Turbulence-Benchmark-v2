from itertools import count

def all_right_truncatable_prime(x: int) -> list[int]:

    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        for i in count(2):
            if i * i > n:
                break
            if n % i == 0:
                return False
        return True

    def right_truncatable(n: int) -> bool:
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[:-i])):
                return False
        return True
    right_truncatable_primes = [n for n in range(2, x) if is_prime(n) and right_truncatable(n)]
    return sorted(right_truncatable_primes, reverse=True)