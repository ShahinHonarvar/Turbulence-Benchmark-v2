def all_left_right_truncatable_prime(nums):
    x = nums[67]
    primes = []

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
        str_n = str(n)
        while len(str_n) > 1:
            if not is_prime(int(str_n)) or '0' in str_n:
                return False
            str_n = str_n[1:-1]
        return is_prime(int(str_n))
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)