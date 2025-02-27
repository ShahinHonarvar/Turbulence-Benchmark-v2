def all_left_right_truncatable_prime(t):
    x = t[8]
    l = []
    for i in range(2, x + 1):
        if str(i).count('0') == 0 and all((int(str(i)[:j]) in l for j in range(1, len(str(i))))) and all((int(str(i)[j:]) in l for j in range(1, len(str(i))))):
            l.append(i)
    return sorted(l, reverse=True)