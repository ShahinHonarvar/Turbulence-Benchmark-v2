def all_left_right_truncatable_prime(nums):
    x = nums[78]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        while n > 9:
            n = int(str(n)[1:])
            if not is_prime(n):
                return False
        n = int(str(n)[:-1])
        while n > 9:
            if not is_prime(n):
                return False
            n = int(str(n)[:-1])
        return True
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)