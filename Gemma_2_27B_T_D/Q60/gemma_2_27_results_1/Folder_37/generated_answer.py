def all_left_right_truncatable_prime(nums):
    x = nums[35]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(x, 1, -1):
        s = str(i)
        if '0' in s:
            continue
        truncatable = True
        while len(s) > 1:
            if not is_prime(int(s)):
                truncatable = False
                break
            s = s[1:-1]
        if truncatable:
            primes.append(i)
    return primes