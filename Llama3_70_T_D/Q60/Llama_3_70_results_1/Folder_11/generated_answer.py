def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):

    def is_truncatable_prime(x):
        str_x = str(x)
        for i in range(1, len(str_x)):
            if not is_prime(int(str_x[i:])):
                return False
            if not is_prime(int(str_x[:-i])):
                return False
        return True
    x = nums[86]
    truncatable_primes = [i for i in range(2, x + 1) if is_prime(i) and is_truncatable_prime(i) and ('0' not in str(i))]
    return truncatable_primes