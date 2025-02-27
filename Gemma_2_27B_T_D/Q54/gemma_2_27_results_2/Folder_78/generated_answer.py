def all_right_truncatable_prime(nums):
    x = nums[23]
    primes = []
    for i in range(2, x):
        n = i
        is_prime = True
        while n > 0:
            if n == 1:
                is_prime = False
                break
            for j in range(2, int(n ** 0.5) + 1):
                if n % j == 0:
                    is_prime = False
                    break
            n //= 10
        if is_prime:
            primes.append(i)
    return sorted(primes)