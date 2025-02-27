def all_left_truncatable_prime(a):
    l = []
    x = a[30]
    for i in range(2, x):
        fact = False
        if '0' not in str(i):
            for j in range(len(str(a))):
                t = str(i)[j:]
                if int(t) > 1 and int(t) % 2 != 0:
                    if int(t) % 3 != 0 and int(t) % 5 != 0 and (int(t) % 7 != 0):
                        if int(t) % 2 ** j != 0 and int(t) % 3 ** j != 0 and (int(t) % 5 ** j != 0) and (int(t) % 7 ** j != 0):
                            pass
                        else:
                            fact = True
                            break
                elif int(t) == 2 or int(t) == 3 or int(t) == 5 or (int(t) == 7):
                    pass
                else:
                    fact = True
                    break
            if not fact:
                l.append(i)
    return sorted(l)