def all_left_truncatable_prime(nums):
    x = nums[71]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(x, 1, -1):
        if '0' not in str(i) and is_prime(i):
            is_truncatable = True
            for j in range(1, len(str(i))):
                if not is_prime(int(str(i)[j:])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)