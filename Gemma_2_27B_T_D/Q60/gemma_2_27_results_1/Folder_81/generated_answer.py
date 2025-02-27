def all_left_right_truncatable_prime(nums):
    x = nums[98]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x + 1):
        if '0' not in str(i) and is_prime(i):
            truncatable = True
            for j in range(1, len(str(i))):
                if not is_prime(int(str(i)[j:])) or not is_prime(int(str(i)[:-j])):
                    truncatable = False
                    break
            if truncatable:
                primes.append(i)
    return sorted(primes)