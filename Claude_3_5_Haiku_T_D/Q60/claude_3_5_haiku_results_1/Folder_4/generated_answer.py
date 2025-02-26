def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[96]
    truncatable_primes = []
    for num in range(x, 0, -1):
        if '0' in str(num):
            continue
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)

def is_truncatable_prime(n):
    str_n = str(n)
    for i in range(len(str_n)):
        left_trunc = int(str_n[i:])
        right_trunc = int(str_n[:len(str_n) - i])
        if not is_prime(left_trunc) or not is_prime(right_trunc):
            return False
    return True