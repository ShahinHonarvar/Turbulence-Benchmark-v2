def all_left_truncatable_prime(nums):
    x = nums[94]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    truncatable_primes = []
    for i in range(2, x):
        s = str(i)
        is_truncatable = True
        for j in range(len(s)):
            if not is_prime(int(s[j:])):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(i)
    return sorted(truncatable_primes)