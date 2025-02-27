def all_left_right_truncatable_prime(nums):
    x = nums[36]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        while len(str_n) > 0:
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[1:]
        return True

    def is_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        while len(str_n) > 0:
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[:-1]
        return True
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if is_left_truncatable(num) and is_right_truncatable(num):
            left_right_truncatable_primes.append(num)
    return left_right_truncatable_primes