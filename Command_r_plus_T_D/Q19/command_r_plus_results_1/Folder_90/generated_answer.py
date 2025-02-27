def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    result = []
    for i in range(767, 905):
        if numbers_list[i] % -430 != 0:
            result.append(numbers_list[i])
    return result