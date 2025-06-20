def all_right_truncatable_prime(nums):
    x = nums[3]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(x, 0, -1):
        if is_prime(i):
            s = str(i)
            is_truncatable = True
            for j in range(len(s) - 1, 0, -1):
                if not is_prime(int(s[:j])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)