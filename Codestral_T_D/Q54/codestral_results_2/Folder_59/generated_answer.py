def all_right_truncatable_prime(nums):
    x = nums[84]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            truncated_num = num
            while truncated_num > 0:
                truncated_num = truncated_num // 10
                if not is_prime(truncated_num):
                    break
            else:
                primes.append(num)
    return sorted(primes, reverse=True)