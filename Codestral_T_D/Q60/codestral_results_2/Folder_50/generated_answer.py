def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        while num > 0:
            if not is_prime(num):
                return False
            num = int(str(num)[1:])
        return True

    def is_right_truncatable_prime(num):
        while num > 0:
            if not is_prime(num):
                return False
            num = int(str(num)[:-1])
        return True
    x = nums[57]
    lrt_primes = [num for num in range(2, x + 1) if is_left_truncatable_prime(num) and is_right_truncatable_prime(num)]
    return sorted(lrt_primes, reverse=True)