def all_right_truncatable_prime(nums):
    x = nums[64]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_str = str(i)
            is_right_truncatable = True
            for k in range(1, len(prime_str)):
                if int(prime_str[:-k]) not in primes:
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)