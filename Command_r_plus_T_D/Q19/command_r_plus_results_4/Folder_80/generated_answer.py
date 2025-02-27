def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    result = []
    for index in range(15, 20):
        if numbers_list[index] % 93 != 0:
            result.append(numbers_list[index])
    return result