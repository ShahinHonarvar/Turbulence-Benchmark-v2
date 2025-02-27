def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    result = []
    for index, num in enumerate(numbers_list[472:828], 472):
        if num % 602 != 0:
            result.append(num)
    return result