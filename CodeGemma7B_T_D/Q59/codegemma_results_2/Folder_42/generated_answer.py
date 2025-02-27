def all_left_truncatable_prime(p):
    a = []
    b = list(str(p[64]))
    for i in range(int(b[0]) + 2):
        if i > 1:
            if i != int(b[0]):
                a.append(i)
    return a