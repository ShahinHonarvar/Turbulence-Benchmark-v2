def all_right_truncatable_prime(nums):
    x = nums[93]
    primes = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            temp = num
            while temp > 0:
                if temp not in primes:
                    break
                temp //= 10
            else:
                primes.append(num)
    return sorted(primes)