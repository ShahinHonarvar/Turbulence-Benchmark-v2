def all_right_truncatable_prime(nums):
    x = nums[3]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            s = str(i)
            truncatable = True
            for j in range(len(s) - 1, 0, -1):
                if not is_prime(int(s[:j])):
                    truncatable = False
                    break
            if truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)