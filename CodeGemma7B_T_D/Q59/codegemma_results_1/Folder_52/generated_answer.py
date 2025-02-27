def all_left_truncatable_prime(tup):
    out = []
    for i in range(52):
        out.append(tuple(sorted(tup[i:52], reverse=True)))
    return out