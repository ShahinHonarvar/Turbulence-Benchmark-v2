def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = nums[30]
    left_truncatable_primes = []
    for n in range(2, x):
        if is_left_truncatable_prime(n):
            left_truncatable_primes.append(n)
    return left_truncatable_primes