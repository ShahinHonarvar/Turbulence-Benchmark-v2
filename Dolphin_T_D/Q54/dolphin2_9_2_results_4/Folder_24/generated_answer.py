def is_tuple_empty(t):
    return len(t) == 0

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

def right_trunc(n):
    return [int(n[i:j]) for i in range(len(n)) for j in range(i + 1, len(n) + 1)]

def all_right_truncatable_prime(t):
    if is_tuple_empty(t):
        return []
    x = t[65]
    l = [i for i in range(2, x) if is_prime(i)]
    r = [i for i in l if all((is_prime(j) for j in right_trunc(str(i))))]
    return sorted(r, reverse=True)