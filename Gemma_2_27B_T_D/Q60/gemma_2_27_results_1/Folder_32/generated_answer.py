def all_left_right_truncatable_prime(nums):
    x = nums[42]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = int(str(n)[1:])
            if n:
                n = int(str(n)[:-1])
        return True
    for i in range(2, x + 1):
        if is_truncatable(i):
            primes.append(i)
    return sorted(primes)