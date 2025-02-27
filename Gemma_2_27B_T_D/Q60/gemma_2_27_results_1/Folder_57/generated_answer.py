def all_left_right_truncatable_prime(nums):
    x = nums[54]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    truncatable_primes = []
    for n in range(2, x + 1):
        n_str = str(n)
        if '0' not in n_str:
            is_truncatable = True
            for i in range(1, len(n_str)):
                if not (is_prime(int(n_str[i:])) and is_prime(int(n_str[:-i]))):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(n)
    return sorted(truncatable_primes, reverse=True)