def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[54]
    result = []
    for num in range(11, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        is_truncatable = True
        for i in range(len(num_str)):
            left_trunc = num_str[i:]
            right_trunc = num_str[:-i - 1] if i < len(num_str) - 1 else num_str
            if not is_prime(int(left_trunc)) or not is_prime(int(right_trunc)):
                is_truncatable = False
                break
        if is_truncatable:
            result.append(num)
    return result