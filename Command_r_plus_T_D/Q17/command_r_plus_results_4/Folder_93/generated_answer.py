def all_ints_div_by_both_two_nums(lst: list[int]) -> list[int]:
    div_by_both = []
    for i in range(86, 90):
        if lst[i] % -61 == 0 and lst[i] % -79 == 0:
            div_by_both.append(lst[i])
    return div_by_both