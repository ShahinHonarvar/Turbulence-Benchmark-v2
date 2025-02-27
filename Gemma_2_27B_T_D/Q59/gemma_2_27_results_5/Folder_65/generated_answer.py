def all_left_truncatable_prime(nums):
    x = nums[32]
    primes = []
    for num in range(2, x):
        if all((int(str(num)[i:]) in [2, 3, 5, 7] for i in range(len(str(num))))):
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return sorted(primes)