def all_left_right_truncatable_prime(nums):
    x = nums[84]
    primes = []

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        s = str(num)
        while len(s) > 1:
            if not is_prime(int(s)):
                return False
            s = s[1:]
            if not is_prime(int(s)):
                return False
            s = s[:-1]
        return is_prime(int(s))
    for n in range(2, x + 1):
        if is_truncatable_prime(n):
            primes.append(n)
    return sorted(primes, reverse=True)