def is_prime(n):
    if n <= 1:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(int_tuple):
    x = int_tuple[370]
    res = []
    for i in range(x, 0, -1):
        if is_prime(i):
            trunc = i
            while trunc > 0:
                if not is_prime(trunc):
                    break
                trunc //= 10
                if trunc == 0:
                    res.append(i)
    return sorted(res, reverse=True)