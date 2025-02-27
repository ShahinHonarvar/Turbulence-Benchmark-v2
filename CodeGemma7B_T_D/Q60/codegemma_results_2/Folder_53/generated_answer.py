from functools import cache
from itertools import count, islice

@cache
def prime_iter():
    for i in count(2):
        if is_prime(i):
            yield i

def get_digits(x):
    if x < 10:
        return [x]
    digits = []
    while x:
        digits.append(x % 10)
        x //= 10
    return digits[::-1]

@cache
def is_truncatable_prime(n):
    digits = get_digits(n)
    if 0 in digits:
        return False

    def is_prime_with_suffix(digits, start):
        if len(digits) <= start:
            return is_prime(int(''.join(map(str, digits))))
        return is_prime_with_suffix(digits[1:], start + 1)
    return all((is_prime_with_suffix(digits, start) for start in range(len(digits))))

def all_left_right_truncatable_prime(n):
    return sorted([i for i in range(n) if is_truncatable_prime(i)], reverse=True)