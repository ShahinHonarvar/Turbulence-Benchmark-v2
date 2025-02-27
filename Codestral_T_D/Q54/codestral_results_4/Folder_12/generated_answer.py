def all_right_truncatable_prime(nums):
    x = nums[70]
    primes = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            truncated_num = num
            while truncated_num > 0:
                if truncated_num not in primes:
                    break
                truncated_num //= 10
            if truncated_num == num:
                primes.append(num)
    primes.sort(reverse=True)
    return primes