def all_left_right_truncatable_prime(nums):
    x = nums[3]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
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
        return True
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)