def all_right_truncatable_prime(nums):
    x = nums[784]
    primes = []
    for i in range(2, x):
        prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            n = i
            while n > 0:
                if n % 2 == 0:
                    break
                for j in range(3, int(n ** 0.5) + 1, 2):
                    if n % j == 0:
                        break
                else:
                    primes.append(i)
                    break
                n //= 10
    return sorted(primes)