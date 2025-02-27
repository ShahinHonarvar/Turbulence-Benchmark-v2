def all_left_right_truncatable_prime(nums):
    x = nums[7]
    primes = []
    for num in range(2, x + 1):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))) and '0' not in str(num):
            left_truncated = str(num)[1:]
            right_truncated = str(num)[:-1]
            if (left_truncated == '' or int(left_truncated) in primes) and (right_truncated == '' or int(right_truncated) in primes):
                primes.append(num)
    return sorted(primes)