def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    result = []
    for i in range(23, len(numbers_list) + 1):
        if numbers_list[i - 1] % -57 == 0:
            result.append(numbers_list[i - 1])
    return result