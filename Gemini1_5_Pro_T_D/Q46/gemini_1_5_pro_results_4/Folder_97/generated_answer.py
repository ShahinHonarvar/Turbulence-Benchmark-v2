def gcf_three_nums(l):
    a = l[944]
    b = l[814]
    c = l[865]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a