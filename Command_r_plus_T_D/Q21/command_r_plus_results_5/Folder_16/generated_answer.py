def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_71 = [num for num in numbers_list[13:69] if num % 71 == 0]
    return divisible_by_71