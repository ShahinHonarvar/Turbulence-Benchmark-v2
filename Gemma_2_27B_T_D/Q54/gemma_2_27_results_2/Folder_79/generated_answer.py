def all_right_truncatable_prime(nums):
    x = nums[91]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            str_i = str(i)
            right_truncatable = True
            for j in range(1, len(str_i)):
                if not int(str_i[:-j]) in primes:
                    right_truncatable = False
                    break
            if right_truncatable:
                primes.append(i)
    return sorted(primes)