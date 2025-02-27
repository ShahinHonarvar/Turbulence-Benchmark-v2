def all_right_truncatable_prime(nums):
    x = nums[803]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            n = str(i)
            is_truncatable = True
            for j in range(len(n) - 1, 0, -1):
                if not is_prime(int(n[:j])):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(i)
    return sorted(truncatable_primes)