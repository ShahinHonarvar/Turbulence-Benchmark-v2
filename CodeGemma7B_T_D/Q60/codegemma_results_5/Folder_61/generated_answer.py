def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_truncatable_prime(num):
    str_num = str(num)
    if '0' in str_num:
        return []

    def check_truncation(num):
        str_num = str(num)
        for i in range(1, len(str_num)):
            trunc_num = int(str_num[i:])
            if not is_prime(trunc_num):
                return False
        return True
    truncatable_primes = []
    for num in range(num, 1, -1):
        if is_prime(num) and check_truncation(num):
            truncatable_primes.append(num)
    return truncatable_primes

def all_left_right_truncatable_prime(nums):
    return get_truncatable_prime(nums[3])