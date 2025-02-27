def all_left_truncatable_prime(nums):
    x = nums[97]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x):
        if is_prime(i):
            s = str(i)
            left_truncatable = True
            for j in range(1, len(s)):
                if not is_prime(int(s[j:])):
                    left_truncatable = False
                    break
            if left_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)