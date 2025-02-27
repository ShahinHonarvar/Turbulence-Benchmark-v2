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

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            left_truncate = int(str_n[i:])
            right_truncate = int(str_n[:len(str_n) - i])
            if not is_prime(left_truncate) or not is_prime(right_truncate):
                return False
        return True
    x = nums[466]
    truncatable_primes = [num for num in range(2, x + 1) if is_truncatable_prime(num)]
    return sorted(truncatable_primes, reverse=True)