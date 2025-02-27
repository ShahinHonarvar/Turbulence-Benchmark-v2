def all_left_truncatable_prime(nums):
    x = nums[88]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(2, x):
        s = str(i)
        if '0' not in s:
            is_truncatable = True
            for j in range(1, len(s)):
                if not is_prime(int(s[j:])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    return sorted(primes)