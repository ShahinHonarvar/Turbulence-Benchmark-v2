def all_right_truncatable_prime(nums):
    x = nums[8]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            str_i = str(i)
            is_right_truncatable = True
            for j in range(len(str_i) - 1, 0, -1):
                if not is_prime:
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                primes.append(i)
    primes.sort(reverse=True)
    return primes