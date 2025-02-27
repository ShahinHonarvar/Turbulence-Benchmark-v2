def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    div_by_both = []
    for i in range(306, 958):
        if numbers_list[i] % 982 == 0 and numbers_list[i] % 319 == 0:
            div_by_both.append(numbers_list[i])
    return div_by_both