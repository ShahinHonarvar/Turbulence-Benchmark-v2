def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[22]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if '0' not in str(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)

def is_truncatable_prime(num):
    num_str = str(num)
    for i in range(1, len(num_str)):
        left_trunc = int(num_str[i:])
        right_trunc = int(num_str[:-i])
        if not (is_prime(left_trunc) and is_prime(right_trunc)):
            return False
    return is_prime(num)