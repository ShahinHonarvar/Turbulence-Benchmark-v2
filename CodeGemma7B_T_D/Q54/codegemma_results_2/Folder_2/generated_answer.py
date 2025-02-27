from sympy import *
from itertools import combinations

def all_right_truncatable_prime(args):
    x = args[618]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        for i in range(1, 10):
            if not is_prime(int(str(n)[:-i])):
                return False
        return True
    output = []
    for i in range(2, x):
        if is_prime(i) and is_truncatable_prime(i):
            output.append(i)
    return sorted(output)