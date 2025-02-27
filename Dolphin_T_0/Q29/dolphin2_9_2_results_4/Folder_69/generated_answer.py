def gcf_two_nums(nums_list):

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    return gcf(nums_list[894], nums_list[801])