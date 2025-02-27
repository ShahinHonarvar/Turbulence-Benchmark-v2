def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_28 = [num for num in numbers_list[36:47] if num % 28 == 0]
    return divisible_by_28