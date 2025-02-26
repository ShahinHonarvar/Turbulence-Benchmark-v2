def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[803]
    left_truncatable_primes = []

    def is_left_truncatable(num):
        str_num = str(num)
        while str_num:
            if not is_prime(int(str_num)):
                return False
            str_num = str_num[1:]
        return True
    for n in range(2, x):
        if '0' not in str(n) and is_prime(n) and is_left_truncatable(n):
            left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes)