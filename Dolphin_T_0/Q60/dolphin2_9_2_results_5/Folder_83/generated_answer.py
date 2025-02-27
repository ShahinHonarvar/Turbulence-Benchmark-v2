def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(t):
    x = t[24]
    l = []
    for i in range(2, x + 1):
        if is_prime(i):
            s = str(i)
            while len(s) > 1:
                if is_prime(int(s[1:])) and is_prime(int(s[:-1])):
                    l.append(i)
                    break
                else:
                    break
    return sorted(l)