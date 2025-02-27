def all_left_right_truncatable_prime(nums):
    x = nums[14]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x + 1):
        s = str(i)
        if '0' in s:
            continue
        is_truncatable = True
        while len(s) > 1:
            if not is_prime(int(s)) or not is_prime(int(s[1:])):
                is_truncatable = False
                break
            s = s[1:-1]
        if is_truncatable:
            primes.append(i)
    return sorted(primes)