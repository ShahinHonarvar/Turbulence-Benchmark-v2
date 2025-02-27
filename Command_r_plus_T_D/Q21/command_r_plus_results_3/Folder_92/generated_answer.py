def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_one = [num for num in numbers_list if num % 1 == 0]
    return divisible_by_one[:1]