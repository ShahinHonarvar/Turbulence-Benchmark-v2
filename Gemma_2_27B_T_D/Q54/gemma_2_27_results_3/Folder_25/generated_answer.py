def all_right_truncatable_prime(nums):
    x = nums[92]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for num in range(2, x):
        if is_prime(num):
            is_truncatable = True
            n = str(num)
            for i in range(len(n) - 1, 0, -1):
                if not is_prime(int(n[:i])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(num)
    return sorted(primes)