def all_right_truncatable_prime(nums):
    x = nums[91]
    truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(2, x):
        is_truncatable = True
        truncated_num = num
        while truncated_num > 0:
            if not is_prime(truncated_num):
                is_truncatable = False
                break
            truncated_num = truncated_num // 10
        if is_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)