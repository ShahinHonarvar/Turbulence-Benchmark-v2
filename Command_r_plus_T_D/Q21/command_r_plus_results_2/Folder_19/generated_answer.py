def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_six = [num for num in numbers_list[1:9] if num % 6 == 0]
    return divisible_by_six