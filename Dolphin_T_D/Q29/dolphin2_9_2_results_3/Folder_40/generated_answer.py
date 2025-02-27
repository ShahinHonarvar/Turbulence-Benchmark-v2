def gcf_two_nums(int_list):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(int_list) < 10:
        return None
    return gcf(int_list[7], int_list[9])