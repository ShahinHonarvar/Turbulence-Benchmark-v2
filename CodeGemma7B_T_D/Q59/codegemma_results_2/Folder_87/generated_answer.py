def all_left_truncatable_prime(t):
    x = t[39]
    L = []
    for n in range(2 ** (len(str(x)) - 1).bit_length()):
        if is_prime(n):
            M = str(n)
            while len(M) >= 2:
                M = M[1:]
                if not is_prime(int(M)):
                    break
            else:
                L.append(n)
    L.sort(reverse=True)
    return L