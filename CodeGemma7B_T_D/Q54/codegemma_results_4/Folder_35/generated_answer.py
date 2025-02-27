def all_right_truncatable_prime(nums):
    x = next(itertools.islice(nums, None, 177))

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    right_truncatable_primes = []
    for num in range(9, x):
        if is_prime(num):
            str_num = str(num)
            truncated_num = int(str_num[:-1])
            if is_prime(truncated_num):
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)