def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    result = []
    for i in range(84, 87):
        if numbers_list[i - 1] % 99 != 0:
            result.append(numbers_list[i - 1])
    return result