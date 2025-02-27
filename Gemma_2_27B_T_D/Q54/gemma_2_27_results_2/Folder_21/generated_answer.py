def all_right_truncatable_prime(nums):
    x = nums[175]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for num in range(2, x):
        if is_prime(num):
            truncatable = True
            n = str(num)
            while len(n) > 1:
                n = n[:-1]
                if not is_prime(int(n)):
                    truncatable = False
                    break
            if truncatable:
                primes.append(num)
    return sorted(primes)