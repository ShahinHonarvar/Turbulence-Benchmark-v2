def all_left_truncatable_prime(a):
    L = [str(i) for i in range(2, a[42])]
    res = []
    for i in L:
        if not '0' in i:
            j = 0
            check = True
            while j < len(i):
                if int(i[j:]) % 2 == 0 or int(i[j:]) % 3 == 0 or int(i[j:]) % 5 == 0 or (int(i[j:]) % 7 == 0 and int(i[j:]) in [2, 3, 5, 7]):
                    check = False
                    break
                j += 1
            if check:
                res.append(i)
    return sorted(res)