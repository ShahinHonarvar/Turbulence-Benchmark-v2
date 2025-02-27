def all_left_right_truncatable_prime(nums):
    x = nums[71]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        n = str(n)
        while len(n) > 1:
            if not is_prime(int(n)) or '0' in n:
                return False
            n = n[1:]
            n = n[:-1]
        return is_prime(int(n))
    for i in range(x, 1, -1):
        if is_truncatable(i):
            primes.append(i)
    return primes