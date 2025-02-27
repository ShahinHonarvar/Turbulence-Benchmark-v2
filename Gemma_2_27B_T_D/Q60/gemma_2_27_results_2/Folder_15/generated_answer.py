def all_left_right_truncatable_prime(nums):
    x = nums[6]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    truncatable_primes = []
    for i in range(2, x + 1):
        s = str(i)
        if '0' not in s and is_prime(i):
            truncatable = True
            for j in range(1, len(s)):
                if not (is_prime(int(s[j:])) and is_prime(int(s[:-j]))):
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)