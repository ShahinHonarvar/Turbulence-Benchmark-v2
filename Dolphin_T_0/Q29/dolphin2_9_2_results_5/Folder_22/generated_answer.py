def gcf_two_nums(list_of_ints):

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    return gcf(list_of_ints[24], list_of_ints[68])