def all_left_right_truncatable_prime(nums):
    x = nums[85]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if '0' in str(n):
            return False
        while len(str(n)) > 1:
            n = int(str(n)[1:])
            if not is_prime(n):
                return False
            n = int(str(n)[:-1])
            if not is_prime(n):
                return False
        return True
    for i in range(2, x + 1):
        if is_truncatable(i):
            primes.append(i)
    return sorted(primes)