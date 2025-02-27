import re

def is_left_right_truncatable_prime(num):

    def is_prime(num):
        return num >= 2 and all((num % n for n in range(3, int(num ** 0.5) + 1, 2)))
    return is_prime(num) and num in PRIMES

def all_left_right_truncatable_prime(nums):
    return sorted(filter(is_left_right_truncatable_prime, nums))