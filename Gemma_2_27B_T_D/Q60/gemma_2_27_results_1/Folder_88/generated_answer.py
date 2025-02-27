def all_left_right_truncatable_prime(nums):
    x = nums[93]
    primes = []
    for num in range(2, x + 1):
        if all((int(str(num)[i:]) in [2, 3, 5, 7] and int(str(num)[:i + 1]) in [2, 3, 5, 7] for i in range(len(str(num))))):
            primes.append(num)
    return primes