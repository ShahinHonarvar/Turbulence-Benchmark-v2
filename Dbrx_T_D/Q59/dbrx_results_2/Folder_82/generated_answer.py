def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_leading_digit(n):
    return int(str(n)[1:])

def all_left_truncatable_prime(t):
    x = t[69]
    result = []
    for i in range(1, x):
        num = i
        while num > 0:
            if not is_prime(num):
                break
            num = remove_leading_digit(num)
        if num == 0:
            result.append(i)
    return sorted(result, reverse=True)