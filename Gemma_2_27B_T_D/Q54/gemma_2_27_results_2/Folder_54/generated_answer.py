def all_right_truncatable_prime(nums):
    x = nums[88]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(x, 1, -1):
        if is_prime(i):
            n = str(i)
            is_right_truncatable = True
            for j in range(len(n) - 1, 0, -1):
                if not is_prime(int(n[:j])):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)