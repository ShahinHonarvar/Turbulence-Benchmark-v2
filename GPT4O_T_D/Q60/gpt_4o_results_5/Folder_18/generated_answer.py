def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_truncatable_prime(num):
    if '0' in str(num) or not is_prime(num):
        return False
    s = str(num)
    for i in range(1, len(s)):
        left_trunc = int(s[i:])
        right_trunc = int(s[:-i])
        if not is_prime(left_trunc) or not is_prime(right_trunc):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[429]
    truncatable_primes = []
    for num in range(x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)