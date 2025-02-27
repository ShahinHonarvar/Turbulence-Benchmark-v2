def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_5 = [num for num in numbers_list if num % 5 == 0]
    return divisible_by_5[:1]