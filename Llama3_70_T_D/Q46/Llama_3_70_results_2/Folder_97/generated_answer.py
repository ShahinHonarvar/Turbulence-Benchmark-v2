def gcf_three_nums(lst):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = lst[944]
    b = lst[814]
    c = lst[865]
    return gcf(gcf(a, b), c)