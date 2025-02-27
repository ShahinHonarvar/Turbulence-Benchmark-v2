def all_left_right_truncatable_prime(nums):
    x = nums[29]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x + 1):
        s = str(i)
        if '0' not in s and is_prime(i):
            left_right_truncatable = True
            for j in range(1, len(s)):
                if not (is_prime(int(s[j:])) and is_prime(int(s[:-j]))):
                    left_right_truncatable = False
                    break
            if left_right_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)