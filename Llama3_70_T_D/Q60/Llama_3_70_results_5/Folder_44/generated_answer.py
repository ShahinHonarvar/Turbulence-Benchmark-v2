def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[39]

    def truncatable(n):
        s = str(n)
        length = len(s)
        if '0' in s:
            return False
        for i in range(length):
            t = int(s[i:])
            if not is_prime(t):
                return False
            t = int(s[:length - i])
            if not is_prime(t):
                return False
        return True
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i) and truncatable(i):
            left_right_truncatable_primes.append(i)
    return left_right_truncatable_primes