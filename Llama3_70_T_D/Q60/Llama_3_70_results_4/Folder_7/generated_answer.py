def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[803]
    result = []
    for i in range(11, x + 1):
        str_i = str(i)
        if '0' in str_i:
            continue
        if not is_prime(i):
            continue
        is_truncatable = True
        while len(str_i) > 2:
            str_i = str_i[1:-1]
            if not is_prime(int(str_i)):
                is_truncatable = False
                break
        if is_truncatable:
            result.append(i)
    return sorted(result)