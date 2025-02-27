def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisibility_condition = lambda num: num % -61 == 0 and num % -64 == 0
    return [num for num in numbers_list[10:29] if divisibility_condition(num)]