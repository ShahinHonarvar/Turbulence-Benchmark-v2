def all_left_truncatable_prime(tups):
    k = tup[65]
    for i in range(2, k):
        if is_prime(i) and (not has_zeros(i)) and is_left_truncatable(i, k):
            tups.append(i)
    tups.sort(reverse=True)
    return [x for x in range(k if k in tuples else 0, k)]