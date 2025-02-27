def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = nums[10]
    primes = []
    for n in range(2, x):
        if is_prime(n):
            trunc = n
            while trunc > 1:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                primes.append(n)
    return sorted(primes, reverse=True)