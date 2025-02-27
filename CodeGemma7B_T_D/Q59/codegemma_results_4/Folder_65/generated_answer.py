def all_left_truncatable_prime(x):
    a = x[32]
    b = []
    for k in range(2, a):
        p = True
        for i in range(2, k // 2 + 1):
            if k % i == 0:
                p = False
                break
        if p:
            for l in range(len(str(k))):
                t = int(str(k)[l:])
                if t < 2:
                    continue
                p = True
                for i in range(2, t // 2 + 1):
                    if t % i == 0:
                        p = False
                        break
                if not p:
                    break
            if p:
                b.append(k)
    b.sort()
    return b