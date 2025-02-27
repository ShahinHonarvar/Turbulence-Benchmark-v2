def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    result = []
    for i in range(21, 51):
        if numbers_list[i] % -77 != 0:
            result.append(numbers_list[i])
    return result