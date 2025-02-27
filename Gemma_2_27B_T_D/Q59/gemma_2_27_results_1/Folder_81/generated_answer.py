def all_left_truncatable_prime(nums):
    x = nums[98]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for num in range(2, x):
        s = str(num)
        is_l_truncatable = True
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                is_l_truncatable = False
                break
        if is_l_truncatable:
            primes.append(num)
    return sorted(primes)