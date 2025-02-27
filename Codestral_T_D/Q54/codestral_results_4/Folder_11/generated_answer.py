def all_right_truncatable_prime(nums):
    x = nums[86]
    primes = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            num_str = str(num)
            if all((int(num_str[i:]) in primes for i in range(1, len(num_str)))):
                primes.append(num)
    return sorted(primes)