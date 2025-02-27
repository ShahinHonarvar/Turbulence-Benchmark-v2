def all_left_right_truncatable_prime(nums):
    x = nums[36]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        while len(s) > 1:
            if not is_prime(int(s)) or not is_prime(int(s[1:])):
                return False
            s = s[1:-1]
        return is_prime(int(s))
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)