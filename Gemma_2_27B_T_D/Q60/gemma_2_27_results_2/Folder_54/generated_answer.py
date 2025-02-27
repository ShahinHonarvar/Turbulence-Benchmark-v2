def all_left_right_truncatable_prime(nums):
    x = nums[88]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        while len(n_str) > 1:
            n_str = n_str[1:]
            if not is_prime(int(n_str)):
                return False
            n_str = n_str[:-1]
            if not is_prime(int(n_str)):
                return False
        return is_prime(int(n_str))
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)