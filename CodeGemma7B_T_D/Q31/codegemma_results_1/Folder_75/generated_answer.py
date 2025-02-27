def if_perfect_num(l):
    if l[80] % l[80] == 0 and l[80] / 2 % 2 != 0 and (l[80] == sum([x for x in range(1, l[80]) if l[80] % x == 0])):
        return True
    return False