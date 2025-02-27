def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    result = []
    for n in range(x, 1, -1):
        if '0' in str(n) or not is_prime(int(str(n)[1:-1])):
            continue
        left_right_truncatable = True
        for i in range(len(str(n)) - 2):
            if not is_prime(int(str(n)[i + 1:-1])):
                left_right_truncatable = False
                break
        if left_right_truncatable:
            result.append(n)
    return result