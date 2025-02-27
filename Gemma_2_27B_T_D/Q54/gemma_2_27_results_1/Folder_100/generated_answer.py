def all_right_truncatable_prime(nums):
    x = nums[26]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(2, x):
        s = str(i)
        truncables = ['-' for _ in range(len(s))]
        for j in range(len(s)):
            truncables[j] = int(s[:len(s) - j])
            if not all((is_prime(t) for t in truncables[:j + 1])):
                break
        else:
            primes.append(i)
    return sorted(primes)