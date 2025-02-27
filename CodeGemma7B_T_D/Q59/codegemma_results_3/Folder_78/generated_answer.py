def all_left_truncatable_prime(t):
    x = t[23]
    [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z] = t
    prime_list = []
    for a in range(2, x):
        if '0' not in str(a):
            temp_list = []
            temp_list.append(str(a))
            for b in range(1, len(str(a))):
                temp_list.append(str(a)[b:])
                if not self.is_prime(int(temp_list.pop())):
                    break
                temp_list.append(str(a)[b:])
            else:
                prime_list.append(a)
    return sorted(prime_list)