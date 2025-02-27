def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisibility_check = lambda x: x % -897 == 0 and x % -556 == 0
    return [num for num in numbers_list[315:935] if divisibility_check(num)]