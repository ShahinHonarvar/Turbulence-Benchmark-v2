def all_left_right_truncatable_prime(t):
    x = t[77]
    ltr = []
    for i in range(2, x + 1):
        if all([int(str(i)[j:] + str(i)[:j]) % j == 0 for j in range(1, len(str(i)))]):
            ltr.append(i)
    return sorted(ltr, reverse=True)