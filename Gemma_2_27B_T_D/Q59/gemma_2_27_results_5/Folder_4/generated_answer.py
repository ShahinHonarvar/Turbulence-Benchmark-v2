def all_left_truncatable_prime(nums):
    x = nums[96]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(x - 1, 0, -1):
        s = str(i)
        if '0' not in s:
            is_left_truncatable = True
            for j in range(len(s)):
                if not is_prime(int(s[j:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)