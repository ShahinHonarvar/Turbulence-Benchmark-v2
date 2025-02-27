def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if n < 10:
            return is_prime(n)
        else:
            n = int(str(n)[1:])
            return is_right_truncatable(n)
    x = nums[29]
    rt_primes = []
    for i in range(1, x):
        if is_right_truncatable(i):
            rt_primes.append(i)
    rt_primes.sort(reverse=True)
    return rt_primes