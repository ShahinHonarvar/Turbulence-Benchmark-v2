def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[177]
    res = []
    for n in range(2, x + 1):
        if is_prime(n):
            str_n = str(n)
            for i in range(1, len(str_n)):
                if str_n[i] == '0':
                    break
                if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
                    break
            else:
                res.append(n)
    return res