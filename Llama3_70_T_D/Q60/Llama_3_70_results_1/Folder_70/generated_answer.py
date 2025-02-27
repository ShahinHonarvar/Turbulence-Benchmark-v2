def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[433]

    def is_left_right_truncatable(n):
        str_n = str(n)
        while len(str_n) > 1:
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[1:-1]
        return True
    truncatable_primes = []
    for i in range(2, x + 1):
        if '0' not in str(i) and is_prime(i) and is_left_right_truncatable(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)