def all_right_truncatable_prime(nums):
    x = nums[96]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x):
        if is_prime(i):
            prime_str = str(i)
            truncatable = True
            while len(prime_str) > 1:
                prime_str = prime_str[:-1]
                if not is_prime(int(prime_str)):
                    truncatable = False
                    break
            if truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)