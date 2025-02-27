def all_left_right_truncatable_prime(t):
    x = t[42]
    lcps = [p for p in range(2, x + 1) if not [d for d in str(p) if d == '0'] and all((isprime(p) for p in range(2, int(str(p)[1:]) + 1)))]
    if not lcps:
        return []
    lrtps = [p for p in lcps if isprime(int(str(p)[:-1])) and isprime(int(str(p)[1:]))]
    return sorted(lrtps)

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True