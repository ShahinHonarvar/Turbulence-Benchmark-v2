def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_truncatable(n):
    n_string = str(n)
    while len(n_string) > 1:
        if not is_prime(int(n_string[1:-1])):
            return False
        n_string = n_string[1:-1]
    return True

def all_left_right_truncatable_prime(t):
    x = t[41]
    result = []
    for n in range(2, x + 1):
        if is_prime(n) and is_truncatable(n):
            result.append(n)
    result.sort()
    return result