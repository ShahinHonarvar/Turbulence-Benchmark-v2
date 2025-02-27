def all_left_right_truncatable_prime(nums):
    x = nums[18]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        sn = str(n)
        return is_prime(int(sn[1:])) and is_prime(int(sn[:-1])) and is_truncatable_prime(int(sn[1:-1]))
    primes = []
    for i in range(x, 1, -1):
        if is_truncatable_prime(i):
            primes.append(i)
    return primes