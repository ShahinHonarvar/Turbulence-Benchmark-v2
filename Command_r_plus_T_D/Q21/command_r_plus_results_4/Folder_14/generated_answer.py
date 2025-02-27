def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_eight = [num for num in numbers_list[8:] if num % 8 == 0]
    return divisible_by_eight