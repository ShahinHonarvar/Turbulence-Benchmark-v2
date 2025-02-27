def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    result = []
    for index, num in enumerate(numbers_list[17:88], 17):
        if num % -75 != 0:
            result.append(num)
    return result