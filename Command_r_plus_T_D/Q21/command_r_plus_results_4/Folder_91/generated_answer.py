def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_five = [num for num in numbers_list if num % 5 == 0]
    return divisible_by_five[:1]