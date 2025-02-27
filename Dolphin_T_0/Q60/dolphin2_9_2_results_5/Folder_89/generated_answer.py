def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        m = int(n ** 0.5)
        for i in range(3, m + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        while len(n_str) > 1:
            if not is_prime(int(n_str)):
                return False
            n_str = n_str[1:-1]
        return is_prime(int(n_str))
    x = nums[97]
    primes = [i for i in range(x, 1, -1) if is_prime(i) and is_truncatable(i)]
    return primes