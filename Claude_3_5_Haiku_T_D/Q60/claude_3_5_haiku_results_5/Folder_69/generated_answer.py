def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(len(str_n)):
        left_trunc = int(str_n[i:])
        right_trunc = int(str_n[:len(str_n) - i])
        if not is_prime(left_trunc) or not is_prime(right_trunc):
            return False
    return is_prime(n)

def all_left_right_truncatable_prime(nums):
    x = nums[760]
    truncatable_primes = []
    for n in range(x, 1, -1):
        if is_left_right_truncatable_prime(n):
            truncatable_primes.append(n)
    return sorted(truncatable_primes, reverse=True)