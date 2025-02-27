def all_right_truncatable_prime(nums):
    x = nums[77]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    result = []
    for prime in primes:
        right_truncatable = True
        temp = str(prime)
        while len(temp) > 0:
            if int(temp) not in primes:
                right_truncatable = False
                break
            temp = temp[:-1]
        if right_truncatable:
            result.append(prime)
    return sorted(result, reverse=True)