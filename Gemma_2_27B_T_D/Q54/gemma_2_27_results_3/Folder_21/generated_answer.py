def all_right_truncatable_prime(nums):
    x = nums[175]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x):
        prime_str = str(i)
        is_truncatable = True
        while len(prime_str) > 0:
            if not is_prime(int(prime_str)):
                is_truncatable = False
                break
            prime_str = prime_str[:-1]
        if is_truncatable:
            primes.append(i)
    return sorted(primes)