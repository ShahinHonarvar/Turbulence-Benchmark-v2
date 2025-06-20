def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if '0' in str(n):
            return False
        n_str = str(n)
        if len(n_str) < 3:
            return is_prime(n)
        for i in range(1, len(n_str)):
            if not is_prime(int(n_str[i:])) or not is_prime(int(n_str[:-i])):
                return False
        return True
    x = nums[88]
    truncatable_primes = [i for i in range(2, x + 1) if is_truncatable(i)]
    return sorted(truncatable_primes, reverse=True)