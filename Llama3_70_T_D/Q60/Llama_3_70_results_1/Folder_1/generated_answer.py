def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[20]

    def is_truncatable_prime(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in range(1, len(n_str)):
            left_truncated = int(n_str[i:])
            right_truncated = int(n_str[:-i])
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                return False
        return True
    truncatable_primes = [i for i in range(2, x + 1) if is_prime(i) and is_truncatable_prime(i)]
    return sorted(truncatable_primes, reverse=True)