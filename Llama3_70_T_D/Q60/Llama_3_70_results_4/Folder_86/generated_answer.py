def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[126]

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        s = str(n)
        while s:
            if not is_prime(int(s)):
                return False
            s = s[1:-1]
        return True
    left_right_truncatable_primes = [i for i in range(2, x + 1) if is_prime(i) and is_left_right_truncatable_prime(i)]
    return sorted(left_right_truncatable_primes, reverse=True)