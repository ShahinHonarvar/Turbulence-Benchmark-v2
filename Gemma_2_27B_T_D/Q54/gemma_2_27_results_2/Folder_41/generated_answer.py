def all_right_truncatable_prime(nums):
    x = nums[46]
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
            n = str(i)
            while len(n) > 0:
                if not is_prime(int(n)):
                    break
                n = n[:-1]
            else:
                primes.append(i)
    primes.sort(reverse=True)
    return primes