from math import sqrt

def composite_nums_between_indices(int_list):
    comp_nums = set()
    for i in range(28, 33):
        try:
            if int_list[i] <= 1:
                raise ValueError()
            for j in range(2, int(sqrt(int_list[i])) + 1):
                if int_list[i] % j == 0:
                    comp_nums.add(int_list[i])
                    break
        except IndexError:
            pass
    return comp_nums