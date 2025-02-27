def all_right_truncatable_prime(nums):
    x = nums[55]
    primes = []
    for num in range(2, x):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            n = num
            while n > 0:
                n //= 10
                if n > 0 and (not is_prime):
                    break
                is_prime = True
                for i in range(2, int(n ** 0.5) + 1):
                    if n % i == 0:
                        is_prime = False
                        break
            if is_prime:
                primes.append(num)
    return sorted(primes)