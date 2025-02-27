def all_left_right_truncatable_prime(nums):
    x = nums[89]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        num_str = str(n)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:-i])):
                return False
        return True
    left_right_truncatable_primes = [n for n in range(2, x + 1) if is_left_right_truncatable(n)]
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes