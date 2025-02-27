def all_right_truncatable_prime(nums):
    x = nums[835]
    primes = []
    for num in range(2, x):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            temp = num
            while temp > 0:
                if temp % 2 == 0 or temp % 3 == 0 or temp % 5 == 0:
                    is_prime = False
                    break
                temp //= 10
            if is_prime:
                primes.append(num)
    return sorted(primes)