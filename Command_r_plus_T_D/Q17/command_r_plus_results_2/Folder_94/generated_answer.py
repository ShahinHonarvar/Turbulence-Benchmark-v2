def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisibility_check = all((num % -53 == 0 and num % -91 == 0 for num in numbers_list[93:95]))
    if divisibility_check:
        return numbers_list[93:95]
    else:
        return []