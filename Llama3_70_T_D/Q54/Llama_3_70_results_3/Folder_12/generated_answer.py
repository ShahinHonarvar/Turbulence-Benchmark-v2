def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[:len(str_n) - i])):
                return False
        return True
    x = nums[70]
    right_truncatable_primes = [i for i in range(x - 1, 1, -1) if is_prime(i) and is_right_truncatable(i)]
    return right_truncatable_primes