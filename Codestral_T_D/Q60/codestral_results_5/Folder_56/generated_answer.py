def all_left_right_truncatable_prime(nums):
    x = nums[30]
    primes = []
    for num in range(2, x + 1):
        if all((int(num[i:]) in primes for i in range(len(num)))) and all((int(num[:i]) in primes for i in range(1, len(num)))):
            primes.append(num)
    return sorted(primes)