def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    str_n = str(n)
    for i in range(len(str_n) - 1):
        if not is_prime(int(str_n[i + 1:])) or not is_prime(int(str_n[:len(str_n) - i - 1])):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[3]
    truncatable_primes = [i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)]
    return sorted(truncatable_primes, reverse=True)