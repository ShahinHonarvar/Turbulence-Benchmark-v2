def all_right_truncatable_prime(nums):
    x = nums[78]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(x - 1, 0, -1):
        s = str(i)
        is_prime_truncatable = True
        for j in range(len(s)):
            if not is_prime(int(s[j:])):
                is_prime_truncatable = False
                break
        if is_prime_truncatable:
            primes.append(i)
    return sorted(primes, reverse=True)