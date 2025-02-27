def gcf_two_nums(int_list):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(int_list[46], int_list[13])