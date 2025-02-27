def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_84 = [num for num in numbers_list[50:55] if num % 84 == 0]
    return divisible_by_84