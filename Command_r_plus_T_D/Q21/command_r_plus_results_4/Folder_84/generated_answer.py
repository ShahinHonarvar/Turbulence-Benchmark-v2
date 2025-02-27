def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_93 = [num for num in numbers_list[52:54] if num % 93 == 0]
    return divisible_by_93