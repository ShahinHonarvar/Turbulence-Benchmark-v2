def all_left_right_truncatable_prime(nums):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable(num):
        num_str = str(num)
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return True

    def is_right_truncatable(num):
        num_str = str(num)
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[:-i])):
                return False
        return True
    x = nums[835]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_prime(num) and is_left_truncatable(num) and is_right_truncatable(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)