def all_left_truncatable_prime(nums):
    x = nums[88]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
        return True
    for i in range(2, x):
        if is_left_truncatable(i):
            primes.append(i)
    return sorted(primes, reverse=True)