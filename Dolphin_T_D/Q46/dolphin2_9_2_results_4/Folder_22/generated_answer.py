def gcf_three_nums(nums_list):
    a = nums_list[27]
    b = nums_list[85]
    c = nums_list[51]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf_ab = gcf(a, b)
    gcf_abc = gcf(gc_ab, c)
    return gcf_abc