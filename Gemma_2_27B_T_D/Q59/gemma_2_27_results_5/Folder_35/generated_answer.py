def all_left_truncatable_prime(nums):
    x = nums[177]
    primes = [2]
    for i in range(3, x, 2):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    ltruncatable = []
    for prime in primes:
        prime_str = str(prime)
        is_ltruncatable = True
        for i in range(1, len(prime_str)):
            if int(prime_str[i:]) not in primes:
                is_ltruncatable = False
                break
        if is_ltruncatable:
            ltruncatable.append(prime)
    return sorted(ltruncatable)