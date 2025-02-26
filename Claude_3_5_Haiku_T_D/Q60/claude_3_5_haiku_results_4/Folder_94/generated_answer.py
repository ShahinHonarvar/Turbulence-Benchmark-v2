def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[43]
    truncatable_primes = []
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        is_lr_truncatable = True
        original_num = num
        while len(str(num)) > 1:
            num = int(str(num)[1:])
            if not is_prime(num):
                is_lr_truncatable = False
                break
        num = original_num
        while len(str(num)) > 1:
            num = int(str(num)[:-1])
            if not is_prime(num):
                is_lr_truncatable = False
                break
        if is_lr_truncatable and is_prime(original_num):
            truncatable_primes.append(original_num)
    return sorted(truncatable_primes)