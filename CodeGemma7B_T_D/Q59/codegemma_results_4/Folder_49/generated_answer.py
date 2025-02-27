def all_left_truncatable_prime(nums):
    x = nums[14]

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable(num):
        num_str = str(num)
        for i in range(1, len(num_str)):
            if int(num_str[i:]) % 2 == 0 or int(num_str[i:]) % 3 == 0:
                return False
            if not is_prime(int(num_str[i:])):
                return False
        return True
    left_truncatable_primes = []
    for num in range(1, x):
        if is_left_truncatable(num):
            left_truncatable_primes.append(num)
    left_truncatable_primes.sort()
    return left_truncatable_primes