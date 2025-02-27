def all_left_right_truncatable_prime(nums):
    x = nums[88]
    primes = []
    for num in range(2, x + 1):
        if all((int(str(num)[:i]) in primes and int(str(num)[i:]) in primes for i in range(1, len(str(num))))):
            primes.append(num)
    return primes