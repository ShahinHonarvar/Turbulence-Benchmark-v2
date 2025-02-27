def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def is_left_right_truncatable(n):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[25]
    truncatable_primes = [i for i in range(11, x + 1) if '0' not in str(i) and is_prime(i) and is_left_right_truncatable(i)]
    return sorted(truncatable_primes, reverse=True)