def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    result = []
    for i in range(70, 72):
        if numbers_list[i] % 85 == 0:
            result.append(numbers_list[i])
    return result