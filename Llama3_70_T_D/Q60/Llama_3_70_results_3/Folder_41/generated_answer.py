def all_left_right_truncatable_prime(nums):
    x = nums[46]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_right_truncatable(n):
        n_str = str(n)
        for _ in range(len(n_str) - 1):
            n_str = n_str[1:]
            if not is_prime(int(n_str)):
                return False
        return True
    left_right_truncatable_primes = [i for i in range(11, x + 1) if set(str(i)) == set(str(i).replace('0', '')) and is_prime(i) and left_right_truncatable(i)]
    return sorted(left_right_truncatable_primes, reverse=True)