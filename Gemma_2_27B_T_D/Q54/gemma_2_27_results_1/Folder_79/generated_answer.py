def all_right_truncatable_prime(nums):
    x = nums[91]
    primes = []
    for i in range(2, x):
        isPrime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            isRightTruncatable = True
            n = i
            while n > 0:
                if n % 2 == 0 or n % 3 == 0 or (n % 5 != 0 and n ** 0.5 < 7 and (n % 7 != 0)):
                    isRightTruncatable = False
                    break
                n //= 10
            if isRightTruncatable:
                primes.append(i)
    return sorted(primes)