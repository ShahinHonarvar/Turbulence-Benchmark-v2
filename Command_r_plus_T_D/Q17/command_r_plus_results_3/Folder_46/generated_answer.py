def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    result = []
    for i in range(11, 47):
        if numbers_list[i] % 55 == 0 and numbers_list[i] % 36 == 0:
            result.append(numbers_list[i])
    return result