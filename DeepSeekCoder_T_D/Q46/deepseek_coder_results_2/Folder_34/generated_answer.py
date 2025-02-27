def gcf_three_nums(nums_list):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(nums_list[53], gcf(nums_list[23], nums_list[45]))