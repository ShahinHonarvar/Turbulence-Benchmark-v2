def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable(n):
        digits = str(n)
        for i in range(len(digits)):
            if not is_prime(int(digits[i:])):
                return False
        return True

    def right_truncatable(n):
        digits = str(n)
        for i in range(len(digits)):
            if not is_prime(int(digits[:-i - 1])):
                return False
        return True
    x = nums[81]
    left_right_truncatable_primes = [i for i in range(2, x + 1) if left_truncatable(i) and right_truncatable(i) and ('0' not in str(i))]
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes