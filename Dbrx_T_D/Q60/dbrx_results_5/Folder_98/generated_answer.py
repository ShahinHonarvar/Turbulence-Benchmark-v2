from itertools import chain

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncate_left_right(n):
    if not is_prime(n):
        return []
    digits = list(str(n))
    for i in range(len(digits)):
        for j in range(len(digits) - i, 0, -1):
            if is_prime(int(''.join(digits[i:j])) and digits[j - 1] != '0'):
                return ' _ '.join(digits[i:j])
    return ''

def all_left_right_truncatable_prime(t):
    x = t[8]
    if x < 10:
        return []
    results = []
    for num in range(10, x + 1):
        if is_prime(num):
            result = truncate_left_right(num)
            if result:
                results.append(result)
    return results[::-1]