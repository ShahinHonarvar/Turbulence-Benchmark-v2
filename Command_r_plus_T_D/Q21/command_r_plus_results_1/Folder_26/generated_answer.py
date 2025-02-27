def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    result = [num for num in numbers_list[45:81] if num % 39 == 0]
    return result