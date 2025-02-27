def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncations(n):
    s = str(n)
    return [int(s[i:]) for i in range(len(s))]

def all_left_truncatable_prime(nums):
    x = nums[88]
    left_truncatable_primes = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        truncations = left_truncations(i)
        if all((is_prime(truncation) for truncation in truncations)):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)