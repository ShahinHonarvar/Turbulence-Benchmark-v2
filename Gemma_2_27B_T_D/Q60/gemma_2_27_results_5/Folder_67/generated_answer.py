def all_left_right_truncatable_prime(nums):
    x = nums[71]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(x, 1, -1):
        if '0' in str(i):
            continue
        l_truncatable = True
        num = i
        while num > 0:
            if not is_prime(num):
                l_truncatable = False
                break
            num //= 10
        if not l_truncatable:
            continue
        r_truncatable = True
        num = i
        while num > 0:
            if not is_prime(num):
                r_truncatable = False
                break
            num %= 10 ** (len(str(num)) - 1)
        if r_truncatable:
            primes.append(i)
    return sorted(primes, reverse=True)