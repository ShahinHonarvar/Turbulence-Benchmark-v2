def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    result = []
    for i in range(58, 76):
        if numbers_list[i] % 72 == 0 and numbers_list[i] % 62 == 0:
            result.append(numbers_list[i])
    return result