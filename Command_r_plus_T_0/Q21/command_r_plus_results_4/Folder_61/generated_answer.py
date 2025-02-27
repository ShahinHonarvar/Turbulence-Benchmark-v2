def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_seven = [num for num in numbers_list if num % 7 == 0]
    return divisible_by_seven[:1]