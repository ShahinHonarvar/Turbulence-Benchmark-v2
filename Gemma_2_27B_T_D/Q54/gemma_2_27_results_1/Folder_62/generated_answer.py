def all_right_truncatable_prime(nums):
    x = nums[70]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x):
        s = str(i)
        is_truncatable = True
        while len(s) > 0:
            if not is_prime(int(s)):
                is_truncatable = False
                break
            s = s[:-1]
        if is_truncatable:
            primes.append(i)
    return sorted(primes)