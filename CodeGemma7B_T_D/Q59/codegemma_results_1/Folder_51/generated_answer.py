def all_left_truncatable_prime(tup):
    x = tup[54]
    listt = []
    for i in range(2, x):
        if isprime(i) and '0' not in str(i):
            b = i
            flag = True
            while b > 0:
                b = int(str(b)[1:])
                if not isprime(b):
                    flag = False
                    break
            if flag:
                listt.append(i)
    listt.sort()
    return listt