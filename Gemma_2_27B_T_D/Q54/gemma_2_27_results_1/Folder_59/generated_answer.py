def all_right_truncatable_prime(nums):
    x = nums[84]
    primes = []
    for num in range(2, x):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    right_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        is_right_truncatable = True
        for i in range(len(str_prime) - 1, 0, -1):
            if int(str_prime[:i]) not in primes:
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)