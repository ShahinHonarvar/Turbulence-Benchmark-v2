def all_left_right_truncatable_prime(nums):
    x = nums[429]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        s = str(n)
        while len(s) > 1:
            if not is_prime(int(s)) or '0' in s:
                return False
            s = s[1:]
            s = s[:-1]
        return is_prime(int(s))
    for i in range(2, x + 1):
        if is_truncatable(i):
            primes.append(i)
    return sorted(primes, reverse=True)