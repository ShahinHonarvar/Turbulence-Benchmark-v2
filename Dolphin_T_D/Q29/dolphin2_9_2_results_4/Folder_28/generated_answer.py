def gcf_two_nums(lst):

    def greatest_common_factor(a, b):
        if b == 0:
            return a
        return greatest_common_factor(b, a % b)
    return greatest_common_factor(lst[48], lst[76])