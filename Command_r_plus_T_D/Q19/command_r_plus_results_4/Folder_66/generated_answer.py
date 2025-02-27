def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    result = []
    for index, number in enumerate(numbers_list[84:87], start=84):
        if number % 99 != 0:
            result.append(number)
    return result