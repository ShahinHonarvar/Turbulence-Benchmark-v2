def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    result = []
    for num in numbers_list[4:8]:
        if num % -6 != 0:
            result.append(num)
    return result