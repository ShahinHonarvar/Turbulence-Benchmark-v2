def all_left_truncatable_prime(nums):
    x = nums[64]
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
        if '0' not in s:
            isPrime = True
            for j in range(len(s)):
                if not is_prime(int(s[j:])):
                    isPrime = False
                    break
            if isPrime:
                primes.append(i)
    return sorted(primes, reverse=True)