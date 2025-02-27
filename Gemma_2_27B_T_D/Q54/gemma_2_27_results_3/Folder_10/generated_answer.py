def all_right_truncatable_prime(nums):
    x = nums[38]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            y = i
            while y > 0:
                if y < 2 or y % 2 == 0:
                    is_prime = False
                    break
                y //= 10
            if is_prime:
                primes.append(i)
    return sorted(primes, reverse=True)