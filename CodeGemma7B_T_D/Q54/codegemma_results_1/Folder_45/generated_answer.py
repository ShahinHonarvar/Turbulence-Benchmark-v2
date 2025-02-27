def all_right_truncatable_prime(a):
    x = a[61]
    li = []
    for i in range(2, x):
        k = True
        for j in str(i):
            if int(j) % 2 == 0:
                k = False
                break
        if k:
            n = i
            while n > 0:
                t = t % 10
                if t % 2 == 0:
                    k = False
                    break
                n //= 10
        if k:
            li.append(i)
    if not li:
        li.append(0)
    return sorted(li)