def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_left_right_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    while len(str_n) > 1:
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[1:-1]
    return is_prime(int(str_n))

def all_left_right_truncatable_prime(nums):
    x = nums[429]
    left_right_truncatable_primes = [i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)]
    return sorted(left_right_truncatable_primes, reverse=True)