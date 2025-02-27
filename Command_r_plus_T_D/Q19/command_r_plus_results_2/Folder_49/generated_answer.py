def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    result = []
    for index, num in enumerate(numbers_list[80:200], 80):
        if num % 1000 != 0:
            result.append(num)
    return result