from typing import List, Tuple

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(limit: int) -> List[int]:
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def is_left_truncatable_prime(n: int) -> bool:
    while n > 0:
        if not is_prime(n):
            return False
        n = n // 10
    return True

def is_right_truncatable_prime(n: int) -> bool:
    while n > 0:
        if not is_prime(n):
            return False
        n = n % (10 * (n // 10))
    return True

def is_left_and_right_truncatable_prime(n: int) -> bool:
    return is_left_truncatable_prime(n) and is_right_truncatable_prime(n)

def all_left_right_truncatable_prime(tup: Tuple[int, ...]) -> List[int]:
    x = tup[645]
    primes = find_primes(x)
    lr_primes = [prime for prime in primes if is_left_and_right_truncatable_prime(prime)]
    return sorted(lr_primes)