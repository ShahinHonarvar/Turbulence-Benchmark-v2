def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(num):
    if '0' in str(num):
        return False
    for i in range(1, len(str(num))):
        left_trunc = int(str(num)[i:])
        right_trunc = int(str(num)[:-i])
        if not is_prime(left_trunc) or not is_prime(right_trunc):
            return False
    return is_prime(num)

def all_left_right_truncatable_prime(nums):
    x = nums[85]
    truncatable_primes = []
    for num in range(11, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)