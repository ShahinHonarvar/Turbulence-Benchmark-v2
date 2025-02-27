def all_left_right_truncatable_prime(nums):
    x = nums[29]
    left_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n <= 1:
            return False
        while n >= 10:
            n = int(str(n)[1:])
            if not is_prime(n):
                return False
        return True

    def is_right_truncatable_prime(n):
        if n <= 1:
            return False
        while n >= 10:
            n = int(str(n)[:-1])
            if not is_prime(n):
                return False
        return True
    for num in range(2, x + 1):
        if is_left_truncatable_prime(num) and is_right_truncatable_prime(num):
            left_truncatable_primes.append(num)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes