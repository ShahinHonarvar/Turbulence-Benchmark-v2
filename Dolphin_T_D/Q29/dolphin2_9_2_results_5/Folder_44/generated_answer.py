def gcf_two_nums(nums_list):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(nums_list[56], nums_list[88])