def all_right_truncatable_prime(nums):
    x = nums[92]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            temp = i
            while temp > 0:
                if temp < 2 or (temp % 2 == 0 and temp != 2):
                    is_prime = False
                    break
                temp //= 10
            if is_prime:
                primes.append(i)
    return sorted(primes)