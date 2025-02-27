def all_right_truncatable_prime(nums):
    x = nums[38]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(x - 1, 0, -1):
        s = str(i)
        if all((is_prime(int(s[:j])) for j in range(len(s), 0, -1))):
            primes.append(i)
    return sorted(primes, reverse=True)