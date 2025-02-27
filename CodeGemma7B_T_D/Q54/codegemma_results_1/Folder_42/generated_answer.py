def all_right_truncatable_prime(tu):
    li = []
    x = tu[64]
    for i in range(2, x + 1):
        for j in range(x // i, 0, -1):
            if x % i == 0 and j % i == 0:
                break
        else:
            li.append(i)
    for i in range(10 ** (len(str(max(li))) - 1)):
        for j in li:
            if int(str(j)[:-i]) % j == 0 or int(str(j)[:-i]) < j:
                li.remove(j)
                break
    return sorted(li, reverse=True) if len(li) > 0 else []