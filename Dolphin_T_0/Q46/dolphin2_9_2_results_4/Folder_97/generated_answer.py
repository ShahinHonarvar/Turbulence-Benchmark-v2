def gcf_three_nums(int_list):
    a = int_list[944]
    b = int_list[814]
    c = int_list[865]

    def gcf(a, b):
        if b == 0:
            return a
        else:
            return gcf(b, a % b)
    return gcf(gcf(a, b), c)