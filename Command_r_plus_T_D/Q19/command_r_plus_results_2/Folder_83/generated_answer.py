def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    result = []
    for index, num in enumerate(numbers_list[90:200], start=90):
        if num % -31 != 0:
            result.append(num)
    return result