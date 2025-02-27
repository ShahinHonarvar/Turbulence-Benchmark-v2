import itertools
import re

def all_left_right_truncatable_prime(nums):
    for p in range(2, int(str(max(nums)) + 1)):
        if PRIMES.match(str(p)):
            yield p
    for p in range(2, int(str(max(nums)) + 1)):
        if PRIMES.match(str(p)[:-1]):
            yield p
    for p in range(2, int(str(max(nums)) + 1)):
        if PRIMES.match(str(p)[-1:]):
            yield p
    for p in range(2, int(str(max(nums)) + 1)):
        for i in range(1, len(str(p)) + 1):
            if PRIMES.match(str(p)[:i]):
                yield p
            if PRIMES.match(str(p)[-i:]):
                yield p
    for p in range(2, int(str(max(nums)) + 1)):
        for i in range(1, len(str(p)) + 1):
            if PRIMES.match(str(p)[:i]):
                yield p
            if PRIMES.match(str(p)[-i:]):
                yield p
    for p in range(2, int(str(max(nums)) + 1)):
        for i in range(1, len(str(p)) + 1):
            if PRIMES.match(str(p)[:i]):
                yield p
            if PRIMES.match(str(p)[-i:]):
                yield p
    for p in range(2, int(str(max(nums)) + 1)):
        for i in range(1, len(str(p)) + 1):
            if PRIMES.match(str(p)[:i]):
                yield p
            if PRIMES.match(str(p)[-i:]):
                yield p
    for p in range(2, int(str(max(nums)) + 1)):
        for i in range(1, len(str(p)) + 1):
            if PRIMES.match(str(p)[:i]):
                yield p
            if PRIMES.match(str(p)[-i:]):
                yield p
    for p in range(2, int(str(max(nums)) + 1)):
        for i in range(1, len(str(p)) + 1):
            if PRIMES.match(str(p)[:i]):
                yield p
            if PRIMES.match(str(p)[-i:]):
                yield p
    for p in range(2, int(str(max(nums)) + 1)):
        for i in range(1, len(str(p)) + 1):
            if PRIMES.match(str(p)[:i]):
                yield p
            if PRIMES.match(str(p)[-i:]):
                yield p