def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[86]
    trunctable_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        if not is_prime(num):
            continue
        left_trunc = str_num
        right_trunc = str_num
        while len(left_trunc) > 1 and len(right_trunc) > 1:
            left_trunc = left_trunc[1:]
            right_trunc = right_trunc[:-1]
            if not is_prime(int(left_trunc)) or not is_prime(int(right_trunc)):
                break
        else:
            trunctable_primes.append(num)
    return sorted(trunctable_primes, reverse=True)