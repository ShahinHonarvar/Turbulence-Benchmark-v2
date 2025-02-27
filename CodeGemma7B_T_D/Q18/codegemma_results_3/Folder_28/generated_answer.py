def sum_ints_div_by_either_nums(lst):
    idx_34 = 34
    idx_81 = 81
    div_27_sum = 0
    div_57_sum = 0
    while idx_34 <= idx_81:
        if lst[idx_34] % 27 == 0:
            div_27_sum += lst[idx_34]
        elif lst[idx_34] % 57 == 0:
            div_57_sum += lst[idx_34]
        idx_34 += 1
    return div_27_sum + div_57_sum