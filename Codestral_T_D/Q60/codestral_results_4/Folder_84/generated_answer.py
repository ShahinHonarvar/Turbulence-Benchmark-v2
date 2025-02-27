def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n % 10 ** (len(str(n)) - 1)
        return True
    x = nums[630]
    left_right_truncatable_primes = []
    for num in range(x, 0, -1):
        if '0' not in str(num) and is_left_truncatable_prime(num) and is_right_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    return left_right_truncatable_primes