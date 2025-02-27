def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not str_n[i].isdigit() or str_n[i] == '0':
                return False
        if is_prime(n):
            for i in range(1, len(str_n)):
                left = int(str_n[i:])
                right = int(str_n[:-i])
                if not (is_prime(left) and is_prime(right)):
                    return False
        else:
            return False
        return True
    x = nums[55]
    truncatable_primes = [i for i in range(2, x + 1) if is_truncatable_prime(i)]
    return truncatable_primes