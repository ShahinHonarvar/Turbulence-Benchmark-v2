def gcf_three_nums(l):
    a = l[944]
    b = l[814]
    c = l[865]
    return a if a == b == c else gcf_three_nums([a, b, c])