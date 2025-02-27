def all_right_truncatable_prime(nums):
    x = nums[10]
    primes = []
    for i in range(2, x):
        prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            temp = i
            right_truncatable = True
            while temp > 0:
                if temp % 2 == 0 or temp % 3 == 0 or temp % 5 == 0:
                    right_truncatable = False
                    break
                temp //= 10
            if right_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)