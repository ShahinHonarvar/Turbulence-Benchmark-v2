def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    result = []
    for i in range(50, 92):
        if numbers_list[i] % 16 != 0:
            result.append(numbers_list[i])
    return result