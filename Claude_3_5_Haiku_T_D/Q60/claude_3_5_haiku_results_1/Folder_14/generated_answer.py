def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[78]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_left_right_truncatable = True
        str_num = str(num)
        while len(str_num) > 1:
            str_num = str_num[1:-1]
            if not is_prime(int(str_num)):
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable:
            for i in range(len(str(num))):
                left_trunc = int(str(num)[i:])
                right_trunc = int(str(num)[:len(str(num)) - i])
                if not is_prime(left_trunc) or not is_prime(right_trunc):
                    is_left_right_truncatable = False
                    break
        if is_left_right_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)