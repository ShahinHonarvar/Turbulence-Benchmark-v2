def all_right_truncatable_prime(nums):
    x = nums[992]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(2, x):
        if is_prime(i):
            j = str(i)
            truncatable = True
            while len(j) > 1:
                j = j[:-1]
                if not is_prime(int(j)):
                    truncatable = False
                    break
            if truncatable:
                primes.append(i)
    return sorted(primes)