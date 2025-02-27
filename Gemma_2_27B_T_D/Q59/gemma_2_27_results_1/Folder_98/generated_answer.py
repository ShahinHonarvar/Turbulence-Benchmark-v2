def all_left_truncatable_prime(nums):
    x = nums[8]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(x - 1, 1, -1):
        s = str(i)
        if '0' not in s and all((is_prime(int(s[:j])) for j in range(1, len(s) + 1))):
            primes.append(i)
    return sorted(primes, reverse=True)