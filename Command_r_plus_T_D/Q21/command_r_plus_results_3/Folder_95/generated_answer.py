def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_num = [num for num in numbers_list[75:86] if num % -40 == 0]
    return divisible_by_num