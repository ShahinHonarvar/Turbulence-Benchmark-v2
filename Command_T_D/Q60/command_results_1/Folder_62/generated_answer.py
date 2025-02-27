import re
import sys
import math
import heapq

def prime_table(x):
    primes = []
    for i in range(2, x + 1):
        if all((n % i for n in range(i ** 2, x + 1, i))):
            primes.append(i)
    return primes

def all_left_right_truncatable_prime(nums):
    primes = prime_table(nums[0])
    primes.sort()
    ltr_primes = []
    for p in primes:
        curr_ltr_primes = []
        for d in str(p):
            if d == '0':
                break
            elif d == '1' or d == '2':
                continue
            else:
                break
        if not curr_ltr_primes:
            break
        ltr_primes.append(p)
    return ltr_primes