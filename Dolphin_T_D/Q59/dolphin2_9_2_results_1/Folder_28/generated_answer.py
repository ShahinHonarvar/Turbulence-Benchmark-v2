def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(n ** 0.5) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True
    primes = [i for i in range(nums[1]) if is_left_truncatable_prime(i)]
    return sorted(primes)