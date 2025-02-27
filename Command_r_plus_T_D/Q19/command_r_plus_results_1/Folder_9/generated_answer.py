def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    not_divisible_by_300 = []
    for index, num in enumerate(numbers_list[70:200], 70):
        if num % -300 != 0:
            not_divisible_by_300.append(num)
    return not_divisible_by_300