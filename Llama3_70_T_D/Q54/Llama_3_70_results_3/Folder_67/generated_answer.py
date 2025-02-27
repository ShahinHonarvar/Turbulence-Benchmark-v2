def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n ** 0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def right_truncatable_prime(n):
    num_str = str(n)
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:])):
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[71]
    right_truncatable_primes = [n for n in range(2, x) if right_truncatable_prime(n)]
    return sorted(right_truncatable_primes, reverse=True)