def gcf_two_nums(list_of_ints):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(list_of_ints[29], list_of_ints[53])