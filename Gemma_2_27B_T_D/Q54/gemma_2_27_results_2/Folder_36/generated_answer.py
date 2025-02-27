def all_right_truncatable_prime(nums):
    x = nums[992]
    primes = []
    for num in range(2, x):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            num_str = str(num)
            is_right_truncatable = True
            for i in range(len(num_str) - 1, 0, -1):
                if not int(num_str[:i]) in primes:
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                primes.append(num)
    return sorted(primes)