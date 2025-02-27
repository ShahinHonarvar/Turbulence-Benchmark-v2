def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_right_truncatable_prime(n):
        if n <= 1:
            return False
        if '0' in str(n):
            return False
        temp = n
        while temp > 0:
            if not is_prime(temp):
                return False
            temp = temp // 10
        temp = n
        while temp > 0:
            if not is_prime(temp):
                return False
            temp = int(str(temp)[1:])
        return True
    x = nums[38]
    left_right_truncatable_primes = [n for n in range(x, 1, -1) if is_left_right_truncatable_prime(n)]
    return left_right_truncatable_primes