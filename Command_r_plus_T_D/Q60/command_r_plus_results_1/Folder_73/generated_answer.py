def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    truncatable_primes = []
    for num in nums:
        if num == 2 or num == 3 or num == 5 or (num == 7):
            truncatable_primes.append(num)
            continue
        str_num = str(num)
        if '0' in str_num:
            continue
        left_truncatable = True
        right_truncatable = True
        for i in range(1, len(str_num)):
            left_trunc = int(str_num[i:])
            right_trunc = int(str_num[:-i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                left_truncatable = False
                right_truncatable = False
                break
        if left_truncatable and right_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)