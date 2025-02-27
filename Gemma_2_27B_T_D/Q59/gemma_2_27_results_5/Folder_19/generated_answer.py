def all_left_truncatable_prime(nums):
    x = nums[67]
    primes = [2, 3, 5, 7]
    for i in range(8, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    left_truncatable_primes = []
    for p in primes:
        p_str = str(p)
        is_left_truncatable = True
        for i in range(1, len(p_str)):
            if int(p_str[i:]) not in primes:
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(p)
    return sorted(left_truncatable_primes, reverse=True)