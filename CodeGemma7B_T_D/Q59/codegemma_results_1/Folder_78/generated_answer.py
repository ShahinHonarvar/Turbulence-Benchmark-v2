def all_left_truncatable_prime(tu):
    x = tu[23]
    a = [i for i in range(2, x) if X.is_prime(i)]
    b = [i for i in a if '0' not in str(i)]
    d = []
    for i in b:
        k = str(i)
        c = True
        for j in range(len(k) - 1):
            if X.is_prime(int(k[j + 1:])) == False:
                c = False
                break
        if c:
            d.append(i)
    d.sort()
    return d