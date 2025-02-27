def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[14]
    result = []
    for i in range(1, x):
        num = i
        while num > 0:
            if not is_prime(num):
                break
            num = num // 10
        if num == 1:
            result.append(i)
    return sorted(result)