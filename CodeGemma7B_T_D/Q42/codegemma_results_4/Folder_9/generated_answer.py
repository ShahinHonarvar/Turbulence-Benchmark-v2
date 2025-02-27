from typing import Set, List

def prime_factors(nums: List[int]) -> Set[int]:
    """Finds the prime factors of the integer at index 24 in the list nums."""
    return {n for n in factorize(nums[24])}

def factorize(n: int) -> Set[int]:
    """Finds all factors of an integer."""
    if n == 0:
        return {0}
    if n == 1:
        return {1}
    if n % 2 == 0:
        return {2, *factorize(n // 2)}
    f = 3
    fs = {1, n}
    while f * f <= n:
        if n % f == 0:
            fs.add(f)
            fs.add(n // f)
        f += 2
    return fs