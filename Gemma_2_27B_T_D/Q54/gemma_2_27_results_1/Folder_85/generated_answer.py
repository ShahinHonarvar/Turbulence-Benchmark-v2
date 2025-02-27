def all_right_truncatable_prime(nums):
    x = nums[94]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x):
        s = str(i)
        is_right_truncatable = True
        for j in range(len(s)):
            if not is_prime(int(s[:len(s) - j])):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            primes.append(i)
    return sorted(primes)