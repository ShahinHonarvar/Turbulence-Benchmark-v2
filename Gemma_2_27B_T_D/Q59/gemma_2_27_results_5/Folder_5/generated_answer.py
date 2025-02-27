def all_left_truncatable_prime(nums):
    x = nums[55]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    truncatable_primes = []
    for num in range(2, x):
        num_str = str(num)
        is_truncatable = True
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[i:])):
                is_truncatable = False
                break
        if is_truncatable and '0' not in num_str:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)