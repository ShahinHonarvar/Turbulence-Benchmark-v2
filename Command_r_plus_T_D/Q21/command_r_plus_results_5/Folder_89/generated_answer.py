def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_39 = [num for num in numbers_list[30:60] if num % 39 == 0]
    return divisible_by_39