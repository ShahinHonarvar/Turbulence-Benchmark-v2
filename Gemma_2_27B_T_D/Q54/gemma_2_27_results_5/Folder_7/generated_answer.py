def all_right_truncatable_prime(nums):
    x = nums[803]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(2, x):
        if is_prime(i):
            prime_str = str(i)
            truncatable = True
            for j in range(1, len(prime_str)):
                if not is_prime(int(prime_str[:-j])):
                    truncatable = False
                    break
            if truncatable:
                primes.append(i)
    return sorted(primes)