def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    result = []
    for index, number in enumerate(numbers_list[387:516], start=387):
        if number % 310 != 0:
            result.append(number)
    return result