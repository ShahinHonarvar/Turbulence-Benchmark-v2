def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    div_by_14 = [num for num in numbers_list[43:77] if num % 14 == 0]
    return div_by_14