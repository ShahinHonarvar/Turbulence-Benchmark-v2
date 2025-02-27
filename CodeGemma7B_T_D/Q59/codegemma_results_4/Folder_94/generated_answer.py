def all_left_truncatable_prime(t):
    ps = []
    for x in range(2, t[43]):
        if all((str(i) in '123456789' for i in str(x))) and str(x)[-1] not in ('2', '5', '0') and all_prime((int(''.join(str(x)[i:])) for i in range(len(str(x))))):
            ps.append(x)
    return sorted(ps)

def all_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True