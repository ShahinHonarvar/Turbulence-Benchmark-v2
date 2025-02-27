from typing import List, Tuple

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncate_right(n: int) -> List[int]:
    result = []
    while n > 0:
        if is_prime(n):
            result.append(n)
        n //= 10
    return result

def all_right_truncatable_prime(tup: Tuple[int]) -> List[int]:
    x = tup[19]
    primes = []
    for i in range(1, x):
        if is_prime(i):
            primes.extend(truncate_right(i))
    return sorted(list(set(primes)))