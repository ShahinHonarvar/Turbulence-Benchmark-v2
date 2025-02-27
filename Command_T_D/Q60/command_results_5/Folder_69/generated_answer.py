import sys
import functools
import bisect

def all_left_right_truncatable_prime(n):
    """
    :type n: tuple
    :rtype: list
    """
    return sorted(set(n).difference(set([x for x in range(3, n[0] // 2 + 1, 2) if all((x % d == 0 for d in range(2, x // 2 + 1) if x % d == 0))])), reverse=True)