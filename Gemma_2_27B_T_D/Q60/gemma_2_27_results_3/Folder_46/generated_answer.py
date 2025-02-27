def all_left_right_truncatable_prime(nums):
    x = nums[33]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' not in str(num):
            num_str = str(num)
            is_truncatable = True
            while len(num_str) > 1:
                if not is_prime(int(num_str)):
                    is_truncatable = False
                    break
                num_str = num_str[1:]
                if not is_prime(int(num_str)):
                    is_truncatable = False
                    break
                num_str = num_str[:-1]
            if is_truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)