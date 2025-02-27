def all_left_truncatable_prime(nums):
    x = nums[36]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for num in range(2, x):
        if '0' not in str(num):
            is_left_truncatable = True
            for i in range(1, len(str(num))):
                if not is_prime(int(str(num)[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable and is_prime(num):
                primes.append(num)
    return sorted(primes)