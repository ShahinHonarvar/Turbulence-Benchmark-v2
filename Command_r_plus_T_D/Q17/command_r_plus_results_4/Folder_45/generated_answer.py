def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    div_by_both_nums = []
    for i in range(30, 201):
        if numbers_list[i] % 115 == 0 and numbers_list[i] % -115 == 0:
            div_by_both_nums.append(numbers_list[i])
    return div_by_both_nums