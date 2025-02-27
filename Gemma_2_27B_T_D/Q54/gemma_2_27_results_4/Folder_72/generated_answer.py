def all_right_truncatable_prime(nums):
    x = nums[31]
    primes = []
    for num in range(2, x):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            truncated_num = num
            while truncated_num > 0:
                if truncated_num % 2 == 0:
                    is_prime = False
                    break
                truncated_num //= 10
                for i in range(2, int(truncated_num ** 0.5) + 1):
                    if truncated_num % i == 0:
                        is_prime = False
                        break
            if is_prime:
                primes.append(num)
    return sorted(primes, reverse=True)