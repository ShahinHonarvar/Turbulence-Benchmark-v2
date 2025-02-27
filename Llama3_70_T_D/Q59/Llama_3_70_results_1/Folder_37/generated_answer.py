def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        num_str = str(n)
        if '0' in num_str:
            return False
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return True
    x = nums[35]
    left_truncatable_primes = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes