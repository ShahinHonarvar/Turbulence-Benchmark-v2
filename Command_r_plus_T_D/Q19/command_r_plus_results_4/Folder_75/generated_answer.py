def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    result = []
    for i in range(20, 51):
        if numbers_list[i] % -48 != 0:
            result.append(numbers_list[i])
    return result