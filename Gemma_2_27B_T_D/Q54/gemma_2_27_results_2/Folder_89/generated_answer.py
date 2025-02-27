def all_right_truncatable_prime(nums):
    x = nums[97]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    right_truncatable_primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            s = str(i)
            is_truncatable = True
            for j in range(1, len(s)):
                if not is_prime(int(s[:len(s) - j])):
                    is_truncatable = False
                    break
            if is_truncatable:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)