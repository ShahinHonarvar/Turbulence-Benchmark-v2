def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    result = []
    for index, number in enumerate(numbers_list[199:201], 199):
        if number % -200 != 0:
            result.append(number)
    return result