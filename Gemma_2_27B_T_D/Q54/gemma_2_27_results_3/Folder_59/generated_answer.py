def all_right_truncatable_prime(nums):
    x = nums[84]
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
            tmp = i
            t = True
            while tmp > 0:
                if not is_prime(tmp):
                    t = False
                    break
                tmp //= 10
            if t:
                primes.append(i)
    return sorted(primes, reverse=True)