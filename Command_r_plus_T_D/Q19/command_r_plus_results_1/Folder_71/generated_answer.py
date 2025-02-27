def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    result = []
    for index, num in enumerate(numbers_list[21:51], start=21):
        if num % -77 != 0:
            result.append(num)
    return result