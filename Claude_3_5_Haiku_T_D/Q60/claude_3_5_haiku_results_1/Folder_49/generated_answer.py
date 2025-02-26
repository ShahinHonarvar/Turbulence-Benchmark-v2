def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[14]
    truncatable_primes = []
    for num in range(10, x + 1):
        if '0' in str(num):
            continue
        is_left_right_truncatable = True
        original_num = num
        while num > 0:
            if not is_prime(num):
                is_left_right_truncatable = False
                break
            num //= 10
        num = original_num
        str_num = str(num)
        while len(str_num) > 0:
            if not is_prime(int(str_num)):
                is_left_right_truncatable = False
                break
            str_num = str_num[1:]
        if is_left_right_truncatable:
            truncatable_primes.append(original_num)
    return sorted(truncatable_primes)