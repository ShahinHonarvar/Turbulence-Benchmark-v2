def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncatable(n):
        str_n = str(n)
        length = len(str_n)
        for i in range(1, length):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
                return False
        return True
    x = nums[88]
    primes = [i for i in range(11, x + 1) if is_prime(i) and '0' not in str(i)]
    result = [i for i in primes if truncatable(i)]
    return sorted(result, reverse=True)