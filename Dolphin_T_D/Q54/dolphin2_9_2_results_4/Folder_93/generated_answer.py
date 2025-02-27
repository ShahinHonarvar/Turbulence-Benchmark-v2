def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[11]
    res = []
    for i in range(2, x - 1):
        if is_prime(i):
            temp = i
            while temp:
                if not is_prime(temp):
                    break
                if not temp:
                    res.append(i)
                    break
                temp //= 10
    return sorted(res)