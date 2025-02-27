def all_left_right_truncatable_prime(nums):
    x = nums[88]
    truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n % 10 ** (len(str(n)) - 1)
        return True
    for num in range(2, x + 1):
        if '0' not in str(num) and is_left_truncatable(num) and is_right_truncatable(num):
            truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes