def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[38]
    res = []
    for i in reversed(range(2, x)):
        if is_prime(i) and str(i).count('0') == 0:
            current = str(i)
            while len(current) > 0 and is_prime(int(current)):
                if len(current) == 1:
                    res.append(i)
                    break
                current = current[1:]
    return res