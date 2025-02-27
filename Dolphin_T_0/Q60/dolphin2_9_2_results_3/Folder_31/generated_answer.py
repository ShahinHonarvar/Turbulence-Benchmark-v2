def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[50]
    result = []
    for i in range(x, 0, -1):
        if i < 10:
            if is_prime(i):
                result.append(i)
        elif (i % 10 != 0 and i // 10 % 10 != 0) and (is_prime(i) and is_prime(i % 10 * 10 ** (len(str(i)) - 1) + int(str(i)[1:-1]))):
            result.append(i)
    return sorted(result, reverse=True)