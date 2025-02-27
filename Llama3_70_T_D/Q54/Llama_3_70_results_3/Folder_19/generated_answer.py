def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    n_str = str(n)
    for i in range(1, len(n_str)):
        if not is_prime(int(n_str[:-i])):
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[67]
    right_truncatable_primes = [i for i in range(2, x) if is_prime(i) and is_right_truncatable(i)]
    return sorted(right_truncatable_primes, reverse=True)