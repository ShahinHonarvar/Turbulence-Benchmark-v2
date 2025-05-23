def all_left_truncatable_prime(nums):
    x = nums[758]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for num in range(2, x):
        if '0' not in str(num):
            is_truncatable = True
            for i in range(len(str(num))):
                if not is_prime(int(str(num)[i:])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(num)
    return sorted(primes)