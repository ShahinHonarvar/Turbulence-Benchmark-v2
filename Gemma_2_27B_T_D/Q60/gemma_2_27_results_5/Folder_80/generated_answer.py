def all_left_right_truncatable_prime(nums):
    x = nums[14]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        s = str(n)
        while len(s) > 1:
            if not is_prime(int(s)):
                return False
            s = s[1:]
        while len(str(n)) > 1:
            if not is_prime(int(str(n)[:-1])):
                return False
            n = int(str(n)[:-1])
        return True
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)