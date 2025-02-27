def all_left_truncatable_prime(nums):
    x = nums[94]
    primes = []
    for num in range(2, x):
        if all((int(str(num)[i:]) > 1 and all((int(str(num)[i:]) % j for j in range(2, int(int(str(num)[i:]) ** 0.5) + 1))) for i in range(len(str(num))))) and '0' not in str(num):
            primes.append(num)
    return sorted(primes)