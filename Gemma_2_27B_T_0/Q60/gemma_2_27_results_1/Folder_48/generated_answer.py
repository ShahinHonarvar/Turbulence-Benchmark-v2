def all_left_right_truncatable_prime(nums):
    x = nums[835]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        n_str = str(n)
        while len(n_str) > 1:
            if not is_prime(int(n_str)):
                return False
            n_str = n_str[1:]
            if not is_prime(int(n_str)):
                return False
            n_str = n_str[:-1]
        return is_prime(int(n_str))
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)