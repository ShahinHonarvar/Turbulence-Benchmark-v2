def all_right_truncatable_prime(nums):
    x = nums[98]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            is_right_truncatable = True
            temp = i
            while temp > 0:
                if not is_prime(temp):
                    is_right_truncatable = False
                    break
                temp //= 10
            if is_right_truncatable:
                primes.append(i)
    return sorted(primes)