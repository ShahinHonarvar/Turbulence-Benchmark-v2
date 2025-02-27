def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    div_by_both = [num for num in numbers_list[138:425] if num % -863 == 0 and num % -329 == 0]
    return div_by_both