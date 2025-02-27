def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n == 1:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_left_truncatable(n):
        while n != 0:
            if is_prime(n):
                n //= 10
            else:
                return False
        return True
    x = nums[784]
    primes = [n for n in range(2, x) if is_prime(n) and str(n).count('0') == 0]
    return [n for n in primes if is_left_truncatable(n)]