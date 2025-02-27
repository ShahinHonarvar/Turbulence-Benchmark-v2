def find_n_th_smallest_num(lst):
    lst.sort(reverse=False)
    required_nums = lst[28:65]
    return required_nums[15]