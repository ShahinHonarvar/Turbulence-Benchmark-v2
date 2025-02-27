def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_2 = [num for num in numbers_list if num % 2 == 0]
    return divisible_by_2[:1]