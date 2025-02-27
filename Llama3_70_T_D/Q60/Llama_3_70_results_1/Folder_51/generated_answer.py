def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[54]

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        while len(str_n) > 0:
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[1:-1]
        return True
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i) and is_truncatable_prime(i):
            truncatable_primes.append(i)
    return truncatable_primes