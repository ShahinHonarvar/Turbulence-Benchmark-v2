def all_right_truncatable_prime(nums):
    x = nums[100]
    primes = []
    for num in range(2, x):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            while num > 0:
                if num % 2 == 0 and num != 2:
                    is_prime = False
                    break
                num //= 10
            if is_prime:
                primes.append(nums[100])
    primes.sort(reverse=True)
    return primes