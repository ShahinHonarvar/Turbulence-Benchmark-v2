def gcf_three_nums(nums_list):

    def gcf(a, b):
        if a == 0:
            return b
        return gcf(b % a, a)
    return gcf(nums_list[78], gcf(nums_list[19], nums_list[13]))