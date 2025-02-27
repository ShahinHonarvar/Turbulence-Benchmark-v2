def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    div_by_both_23_57 = [num for num in numbers_list[77:88] if num % 23 == 0 and num % 57 == 0]
    return div_by_both_23_57