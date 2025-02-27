def all_left_right_truncatable_prime(nums):
    x = nums[55]
    primes = [True] * (x + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, x + 1, i):
                primes[j] = False

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        n_str = str(n)
        while len(n_str) > 1:
            if not primes[int(n_str)] and (not primes[int(n_str[::-1])]):
                return False
            n_str = n_str[1:]
            n_str = n_str[:-1]
        return primes[int(n_str)]
    return sorted([n for n in range(2, x + 1) if is_truncatable_prime(n)])