def all_right_truncatable_prime(t):
    x = t[100]
    res = []
    for k in range(x // 2, 0, -1):
        for b in str(k)[::-1]:
            if int(b.lstrip('0')) > 1 and b.lstrip('0').isnumeric():
                num = int(b.lstrip('0'))
                if is_prime(num) and is_truncatable_prime(b.lstrip('0')):
                    res.append(num)
    return sorted(res, reverse=True) or []

def is_prime(num):
    if num <= 1:
        return False
    i = 2
    limit = num ** 0.5
    while i <= limit:
        if num % i == 0:
            return False
        i += 1
    return True

def is_truncatable_prime(num):
    for i in range(len(num), 0, -1):
        if not is_prime(int(num[:i])):
            return False
    return True