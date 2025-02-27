def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    result = [num for num in numbers_list if num % 6 == 0]
    return result