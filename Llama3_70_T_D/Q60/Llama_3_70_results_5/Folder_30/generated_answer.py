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

def all_left_right_truncatable_prime(nums):
    x = nums[37]

    def is_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
                return False
        return True
    truncatable_primes = [i for i in range(2, x + 1) if is_prime(i) and is_truncatable(i)]
    return sorted(truncatable_primes, reverse=True)