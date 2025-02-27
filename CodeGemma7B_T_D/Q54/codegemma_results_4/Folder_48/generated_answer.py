def all_right_truncatable_prime(tup):
    x = tup[835]
    r_tp = []
    for i in range(2, x):
        if i in tup[:x]:
            continue
        if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))):
            a = str(i)
            for j in range(1, len(a)):
                if all((int(a[:j]) % k != 0 for k in range(2, int(i ** 0.5) + 1))):
                    r_tp.append(int(a[:j]))
    return r_tp