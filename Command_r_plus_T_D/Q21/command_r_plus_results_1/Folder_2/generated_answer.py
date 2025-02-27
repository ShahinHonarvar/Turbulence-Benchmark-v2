def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_58 = [num for num in numbers_list[62:71] if num % 58 == 0]
    return divisible_by_58