def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    result = []
    for index, num in enumerate(numbers_list[199:201], 199):
        if num % -200 != 0:
            result.append(num)
    return result