def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[33]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        is_truncatable = True
        left_trunc = num
        while left_trunc > 0:
            if not is_prime(left_trunc):
                is_truncatable = False
                break
            left_trunc //= 10
        right_trunc = num
        while right_trunc > 0:
            if not is_prime(right_trunc):
                is_truncatable = False
                break
            right_trunc %= 10 ** (len(str(right_trunc)) - 1)
        if is_truncatable:
            result.append(num)
    return sorted(result)