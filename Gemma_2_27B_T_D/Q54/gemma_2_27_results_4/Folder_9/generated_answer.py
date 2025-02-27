def all_right_truncatable_prime(nums):
    x = nums[29]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            n = i
            while n > 0:
                if n % 2 == 0:
                    break
                if n < 2:
                    break
                n //= 10
                for j in range(2, int(n ** 0.5) + 1):
                    if n % j == 0:
                        is_prime = False
                        break
                if not is_prime:
                    break
            if is_prime:
                primes.append(i)
    return sorted(primes, reverse=True)