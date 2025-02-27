def all_left_right_truncatable_prime(nums):
    x = nums[758]
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
        if '0' not in s:
            is_truncatable = True
            for j in range(1, len(s)):
                if not is_prime(int(s[j:])) or not is_prime(int(s[:-j])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    return sorted(primes)