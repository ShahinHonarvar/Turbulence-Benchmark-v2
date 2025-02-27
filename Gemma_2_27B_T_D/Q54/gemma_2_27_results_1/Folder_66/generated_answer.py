def all_right_truncatable_prime(nums):
    x = nums[25]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            i_str = str(i)
            is_truncatable = True
            for k in range(1, len(i_str)):
                if not int(i_str[:-k]) in primes:
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)