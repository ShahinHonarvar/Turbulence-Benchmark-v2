from functools import reduce
from itertools import islice

def rm_one(number):
    return number // 10

def is_prime(number):
    divisors = (d for d in range(2, int(number ** 0.5) + 1) if number % d == 0)
    return not bool(list(divisors))

def is_truncatable_prime(number):
    temp = number
    while temp > 0:
        if not is_prime(temp):
            return False
        temp = rm_one(temp)
    return True

def filter_right_truncatable_prime(number):
    return is_prime(number) and is_truncatable_prime(number)

def all_right_truncatable_prime(numbers):
    right_truncatable_primes = (number for number in numbers if filter_right_truncatable_prime(number))
    return sorted(islice(right_truncatable_primes, 758))