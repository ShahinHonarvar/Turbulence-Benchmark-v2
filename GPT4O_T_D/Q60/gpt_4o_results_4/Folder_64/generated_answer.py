def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n <= 1:
            return False
        if n < 4:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_right_truncatable(p):
        s = str(p)
        if '0' in s:
            return False
        n = len(s)
        for i in range(n):
            truncated_l = int(s[i:])
            truncated_r = int(s[:n - i])
            if not is_prime(truncated_l) or not is_prime(truncated_r):
                return False
        return True
    x = nums[4]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i) and is_left_right_truncatable(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)