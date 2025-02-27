def all_left_truncatable_prime(nums):
    x = nums[784]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x):
        s = str(i)
        if '0' not in s and all((is_prime(int(s[j:])) for j in range(len(s)))):
            primes.append(i)
    return sorted(primes)