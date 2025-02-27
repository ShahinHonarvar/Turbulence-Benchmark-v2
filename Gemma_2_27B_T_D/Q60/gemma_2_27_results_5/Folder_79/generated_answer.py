def all_left_right_truncatable_prime(nums):
    x = nums[91]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        n = str(n)
        while len(n) > 1:
            if not is_prime(int(n)) or '0' in n:
                return False
            n = n[1:-1]
        return is_prime(int(n))
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)