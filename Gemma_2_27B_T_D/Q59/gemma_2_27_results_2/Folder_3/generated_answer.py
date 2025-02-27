def all_left_truncatable_prime(nums):
    x = nums[100]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for num in range(2, x):
        if '0' not in str(num) and is_prime(num):
            truncated = str(num)
            is_truncatable = True
            for i in range(1, len(truncated)):
                if not is_prime(int(truncated[i:])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(num)
    return sorted(primes)