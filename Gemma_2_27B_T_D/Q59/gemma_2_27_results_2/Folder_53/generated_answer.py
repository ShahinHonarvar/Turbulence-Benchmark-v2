def all_left_truncatable_prime(nums):
    x = nums[86]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x):
        if '0' not in str(i):
            is_truncatable = True
            num = str(i)
            while len(num) > 0:
                if not is_prime(int(num)):
                    is_truncatable = False
                    break
                num = num[1:]
            if is_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)