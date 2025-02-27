def all_right_truncatable_prime(nums):
    x = nums[46]
    primes = []

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    for num in range(2, x):
        if is_prime(num):
            is_truncatable = True
            num_str = str(num)
            for i in range(1, len(num_str)):
                if not is_prime(int(num_str[:-i])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)