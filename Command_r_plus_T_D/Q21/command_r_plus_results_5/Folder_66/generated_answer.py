def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    div_by_18 = [num for num in numbers_list[14:69] if num % 18 == 0]
    return div_by_18