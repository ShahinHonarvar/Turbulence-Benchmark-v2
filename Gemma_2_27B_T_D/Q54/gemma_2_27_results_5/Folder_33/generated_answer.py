def all_right_truncatable_prime(nums):
    x = nums[945]
    primes = []
    for num in range(2, x):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            truncatable = True
            n = num
            while n > 0:
                if n % 2 == 0 or n % 3 == 0 or (n > 5 and n % 5 == 0):
                    truncatable = False
                    break
                n //= 10
            if truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)