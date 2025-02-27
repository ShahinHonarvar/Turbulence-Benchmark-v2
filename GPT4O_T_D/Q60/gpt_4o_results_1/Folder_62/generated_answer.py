def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if not s:
                break
            if '0' in s or not is_prime(int(s)):
                return False
        return True
    x = nums[70]
    left_right_truncatable_primes = []
    for i in range(11, x + 1):
        if '0' not in str(i) and is_prime(i) and is_left_right_truncatable(i):
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes)