def all_left_truncatable_prime(nums):
    x = nums[43]

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = []
    for num in range(2, x):
        num_str = str(num)
        if '0' not in num_str:
            is_left_truncatable = True
            for i in range(1, len(num_str)):
                if not is_prime(int(num_str[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(num)
    return sorted(primes)