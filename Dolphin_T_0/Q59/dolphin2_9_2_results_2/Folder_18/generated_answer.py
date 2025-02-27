def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[429]
    res = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            n = num
            while n:
                n = n // 10
                if not is_prime(n):
                    break
                if n == 0:
                    res.append(num)
    return sorted(res, reverse=True)