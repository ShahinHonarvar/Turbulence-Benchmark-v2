def gcf_three_nums(lst):

    def gcf_two_nums(a, b):
        if b == 0:
            return a
        return gcf_two_nums(b, a % b)
    return gcf_two_nums(gcf_two_nums(lst[38], lst[52]), lst[69])