def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    non_divisible_by_10 = [num for num in numbers_list[1:10] if num % 10 != 0]
    return non_divisible_by_10