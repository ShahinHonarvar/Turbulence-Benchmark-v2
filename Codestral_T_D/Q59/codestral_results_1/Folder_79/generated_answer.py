def all_left_truncatable_prime(nums):
    x = nums[91]
    primes = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))) and '0' not in str(num):
            truncated = str(num)
            while truncated:
                if int(truncated) not in primes:
                    break
                truncated = truncated[1:]
            else:
                primes.append(num)
    return sorted(primes)