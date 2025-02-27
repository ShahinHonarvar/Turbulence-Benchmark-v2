def all_left_right_truncatable_prime(t):
    x = t[73]
    l = []
    for n in reversed(range(2, x + 1)):
        if n in l:
            continue
        for d in l:
            if str(d) in str(n):
                break
        else:
            prime = is_prime(n)
            if not n // 10 or not n % 10 or (not prime):
                continue
            m = n
            while m > 9:
                m = m // 10 if m % 10 == m else m * 10 + m % 10 - 1
                if not is_prime(m):
                    break
            else:
                l.append(n)
    return sorted(l, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True