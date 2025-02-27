def all_left_truncatable_prime(nums):
    x = nums[6]
    primes = [2, 3, 5, 7]
    for i in range(2, x):
        if all((j != 0 and i % j for j in range(2, int(i ** 0.5) + 1))):
            primes.append(i)
    result = []
    for p in primes:
        p = str(p)
        flag = True
        for i in range(1, len(p)):
            if int(p[i:]) not in primes:
                flag = False
                break
        if flag:
            result.append(int(p))
    return sorted(result, reverse=True)