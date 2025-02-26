def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[32]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        is_truncatable = True
        for i in range(len(str(num))):
            trunc_left = int(str(num)[i:])
            if not is_prime(trunc_left):
                is_truncatable = False
                break
        for i in range(len(str(num))):
            trunc_right = int(str(num)[:len(str(num)) - i])
            if not is_prime(trunc_right):
                is_truncatable = False
                break
        if is_truncatable:
            result.append(num)
    return sorted(result)