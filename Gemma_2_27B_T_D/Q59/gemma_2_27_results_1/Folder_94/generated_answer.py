def all_left_truncatable_prime(nums):
    x = nums[43]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x):
        if '0' not in str(i):
            is_truncatable = True
            for j in range(1, len(str(i))):
                if not is_prime(int(str(i)[j:])):
                    is_truncatable = False
                    break
            if is_truncatable and is_prime(i):
                primes.append(i)
    return sorted(primes)