def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[28]
    result = []
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        is_truncatable = True
        temp = num
        while temp > 0:
            if not is_prime(temp):
                is_truncatable = False
                break
            temp //= 10
        temp = num
        digits = len(str(temp))
        while digits > 1:
            temp %= 10 ** (digits - 1)
            if not is_prime(temp):
                is_truncatable = False
                break
            digits -= 1
        if is_truncatable:
            result.append(num)
    return sorted(result)