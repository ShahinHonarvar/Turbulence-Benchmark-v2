def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    div_by_901 = [num for num in numbers_list[601:699] if num % 901 == 0]
    return div_by_901