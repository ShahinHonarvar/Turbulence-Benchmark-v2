def all_left_right_truncatable_prime(x):
    d = {i: i for i in range(2, x + 1)}
    r = [i]
    for i in range(2, x + 1):
        for j in range(2, i):
            if i % j == 0:
                del d[i]
                break
    for i in d:
        u = str(i)
        v = u[::-1]
        if u == v:
            continue
        if u[0] == '0' or v[0] == '0':
            continue
        if int(u[-1]) == int(v[0]) and u[-1] != '0' and (v[0] != '0'):
            if int(u[0:-1]) in r and int(v[1:]) in r:
                r.append(int(u))
    if r == [i] and i == x:
        return []
    else:
        return sorted(r)