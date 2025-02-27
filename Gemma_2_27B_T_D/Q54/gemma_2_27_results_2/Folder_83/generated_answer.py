def all_right_truncatable_prime(nums):
    x = nums[24]
    primes = []
    for i in range(2, x):
        if all((i % j for j in range(2, int(i ** 0.5) + 1))) and all((int(str(i)[:-k]) > 1 and int(str(i)[:-k]) in [j for j in range(2, int(int(str(i)[:-k]) ** 0.5) + 1)] == False for k in range(1, len(str(i))))):
            primes.append(i)
    return sorted(primes)