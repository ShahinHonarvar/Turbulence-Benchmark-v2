def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(p):
        str_p = str(p)
        for i in range(len(str_p)):
            left = str_p[i:]
            right = str_p[:len(str_p) - i]
            if '0' in left or '0' in right:
                return False
            if not is_prime(int(left)) or not is_prime(int(right)):
                return False
        return True
    x = nums[10]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)