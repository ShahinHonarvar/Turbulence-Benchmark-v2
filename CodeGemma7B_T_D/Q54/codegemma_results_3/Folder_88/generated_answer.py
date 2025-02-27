def all_right_truncatable_prime(test):
    list1 = []
    for i in range(test[0]):
        n = 10 ** i
        for j in range(2, test[0]):
            l = j
            f = True
            for k in range(i):
                if l % 10 not in [2, 3, 5, 7]:
                    f = False
                    break
                l = l // 10
            if not f:
                continue
            for a in range(2, int(j ** 0.5) + 1):
                if j % a == 0:
                    f = False
                    break
            if f and j not in list1:
                list1.append(j)
    list1.sort()
    return list1