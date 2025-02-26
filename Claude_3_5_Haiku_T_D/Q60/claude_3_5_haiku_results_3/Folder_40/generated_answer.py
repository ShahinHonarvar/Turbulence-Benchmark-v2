def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[10]
    result = []
    for num in range(x, 11, -1):
        str_num = str(num)
        if '0' in str_num:
            continue
        if not is_prime(num):
            continue
        is_truncatable = True
        for left in range(len(str_num)):
            for right in range(len(str_num), left, -1):
                truncated = int(str_num[left:right])
                if not is_prime(truncated):
                    is_truncatable = False
                    break
            if not is_truncatable:
                break
        if is_truncatable:
            result.append(num)
    return result