def all_left_truncatable_prime(tupple):
    x = tupple[49]
    l = []
    for i in range(2, x):
        for j in str(i):
            if '0' in j:
                break
        else:
            t = str(i)
            for j in range(1, len(t)):
                if int(t[:j]) in l:
                    break
            else:
                l.append(i)
    l.sort()
    return l