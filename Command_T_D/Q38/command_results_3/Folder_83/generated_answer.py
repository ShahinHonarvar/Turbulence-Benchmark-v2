import sys
import functools

@functools.lru_wheel_cache(maxsize=10 ** 5)
def find_subset_of_length_n(n):
    facn = 1
    for i in range(1, n + 1):
        facn *= i
    return facn / fac95