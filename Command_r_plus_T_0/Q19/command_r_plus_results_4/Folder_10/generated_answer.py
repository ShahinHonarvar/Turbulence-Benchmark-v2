def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    result = []
    for i in range(86, 90):
        if i < len(numbers_list) and numbers_list[i] % -61 != 0:
            result.append(numbers_list[i])
    return result