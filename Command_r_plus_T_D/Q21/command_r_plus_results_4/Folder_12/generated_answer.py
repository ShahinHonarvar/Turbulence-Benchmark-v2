def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_num = [num for num in numbers_list[23:66] if num % -46 == 0]
    return divisible_by_num