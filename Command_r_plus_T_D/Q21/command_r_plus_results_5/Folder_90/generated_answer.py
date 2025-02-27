def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    div_by_num_list = []
    for index, num in enumerate(numbers_list[417:891], 417):
        if num % -173 == 0:
            div_by_num_list.append(num)
    return div_by_num_list