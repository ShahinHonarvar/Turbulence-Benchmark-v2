def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):

    def is_left_truncatable_prime(num):
        if '0' in str(num):
            return False
        str_num = str(num)
        while str_num:
            if not is_prime(int(str_num)):
                return False
            str_num = str_num[1:]
        return True
    x = nums[26]
    truncatable_primes = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)