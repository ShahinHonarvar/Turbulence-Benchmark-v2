def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    result = [num for num in numbers_list[46:92] if num % 67 == 0 and num % 15 == 0]
    return result