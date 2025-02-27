from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    nums = set()
    for digit in range(1, len(str(n))):
        nums.add(int(str(n)[:-digit]))
        nums.add(int(str(n)[digit:]))
    return all((is_prime(num) for num in nums))

def all_left_right_truncatable_prime(tp):
    x = tp[7]
    return sorted([n for n in range(2, x + 1) if is_truncatable_prime(n)]) or []