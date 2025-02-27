def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    div_by_85_list = [num for num in numbers_list[70:72] if num % 85 == 0]
    return div_by_85_list