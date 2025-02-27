def all_right_truncatable_prime(nums):
    x = nums[30]
    primes = []

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    for i in range(2, x):
        n = i
        is_right_truncatable = True
        while n > 0:
            if not is_prime(n):
                is_right_truncatable = False
                break
            n //= 10
        if is_right_truncatable:
            primes.append(i)
    return sorted(primes)