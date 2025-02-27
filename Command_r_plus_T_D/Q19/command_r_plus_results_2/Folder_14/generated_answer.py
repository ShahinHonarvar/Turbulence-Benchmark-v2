def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    result = []
    for i in range(2, 8):
        if numbers_list[i] % 8 != 0:
            result.append(numbers_list[i])
    return result