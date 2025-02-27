def all_right_truncatable_prime(nums):
    x = nums[73]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_truncatable_primes(n):
        truncatable_primes = []
        for i in range(2, int(n + 0.5)):
            if is_prime(i) and all((is_prime(int(str(i)[:-j])) for j in range(1, len(str(i))))):
                truncatable_primes.append(i)
        return sorted(truncatable_primes, reverse=True)
    return get_truncatable_primes(x)