def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    result = []
    for i in range(43, 70):
        if i < len(numbers_list) and numbers_list[i] % 69 != 0:
            result.append(numbers_list[i])
    return result