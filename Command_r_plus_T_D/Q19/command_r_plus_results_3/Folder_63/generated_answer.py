def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    result = []
    for index in range(20, 43):
        if numbers_list[index] % 95 != 0:
            result.append(numbers_list[index])
    return result