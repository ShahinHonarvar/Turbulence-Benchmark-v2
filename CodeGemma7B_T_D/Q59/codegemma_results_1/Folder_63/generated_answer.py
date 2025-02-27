def all_left_truncatable_prime(t):
    x = t[88]
    prime_l = [i for i in range(2, x) if all((str(i)[-j] in '2357' for j in range(1, len(str(i)))))]
    return [i for i in prime_l if all_truncatable(i)]

def all_truncatable(k):
    if int(str(k)[-1]) % 2 == 0:
        return False
    t = str(k)
    for i in range(1, len(t)):
        if int(t[:i]) not in prime_l:
            return False
    return True