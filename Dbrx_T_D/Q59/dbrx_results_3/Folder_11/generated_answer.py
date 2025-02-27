def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    result = []
    for num in range(1, n):
        if str(num)[0] == '0':
            continue
        is_left_truncatable = True
        for digit in range(len(str(num))):
            if not is_prime(int(str(num)[digit:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            result.append(num)
    return sorted(result)