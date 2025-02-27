def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n > 2 and n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

def all_left_truncatable_prime(t):
    x = t[57]
    res = []
    for num in range(x, 1, -1):
        if is_prime(num) and str(num).count('0') == 0:
            left_trunc = str(num)
            while left_trunc:
                if not is_prime(int(left_trunc)):
                    break
                if not left_trunc or left_trunc[0] == '0':
                    res.append(num)
                    break
                left_trunc = left_trunc[1:]
    return sorted(res, reverse=True)