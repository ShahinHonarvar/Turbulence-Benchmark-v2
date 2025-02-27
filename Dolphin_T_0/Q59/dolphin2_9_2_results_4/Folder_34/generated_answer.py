def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        n_str = str(n)
        while n_str:
            if not is_prime(int(n_str)):
                return False
            n_str = n_str[1:]
        return True
    x = nums[18]
    primes = [i for i in range(2, x) if is_prime(i) and is_left_truncatable(i)]
    return sorted(primes, reverse=True)