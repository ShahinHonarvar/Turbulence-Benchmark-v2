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
        while len(str_n) > 1:
            str_n = str_n[1:-1]
            if not str_n:
                return True
            if not is_prime(int(str_n)):
                return False
        return True

    def contains_zero(n):
        return '0' in str(n)
    if len(nums) <= 630 or nums[630] <= 1:
        return []
    x = nums[630]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_prime(num) and (not contains_zero(num)) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)