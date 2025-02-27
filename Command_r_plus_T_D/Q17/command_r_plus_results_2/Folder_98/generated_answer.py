def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    result = []
    for i in range(6):
        if numbers_list[i] % -1 == 0 and numbers_list[i] % 13 == 0:
            result.append(numbers_list[i])
    return result