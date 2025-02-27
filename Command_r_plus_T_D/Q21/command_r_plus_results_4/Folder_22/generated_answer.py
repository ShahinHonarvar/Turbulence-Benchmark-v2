def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_numbers = [num for num in numbers_list[10:21] if num % 1 == 0]
    return divisible_numbers