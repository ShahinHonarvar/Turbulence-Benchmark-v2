def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

def all_left_right_truncatable_prime(t):
    x = t[70]
    prime_set = set()
    for num in range(2, x + 1):
        x = str(num)
        if '0' in x:
            continue
        while len(x) > 1:
            if x[0] != '0' and x[-1] != '0':
                if not is_prime(int(x[:-1])) or not is_prime(int(x[1:])):
                    break
                if len(x) == 2:
                    prime_set.add(num)
                x = x[1:-1]
            else:
                break
    return sorted(prime_set, reverse=True)