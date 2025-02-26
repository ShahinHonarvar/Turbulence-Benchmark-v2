def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[93]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if not is_prime(num):
            continue
        truncatable = True
        temp_left = num
        temp_right = num
        while len(str(temp_left)) > 1:
            temp_left //= 10
            if not is_prime(temp_left):
                truncatable = False
                break
        while len(str(temp_right)) > 1:
            temp_right %= 10 ** (len(str(temp_right)) - 1)
            if not is_prime(temp_right):
                truncatable = False
                break
        if truncatable:
            result.append(num)
    return sorted(result)