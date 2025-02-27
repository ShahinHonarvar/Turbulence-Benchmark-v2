def all_left_truncatable_prime(n):
    list = []
    for i in range(2, int(str(n[0])[0]) + 1):
        if all((str(j) for j in range(2, i))):
            list += [i]
    list.sort()
    return list