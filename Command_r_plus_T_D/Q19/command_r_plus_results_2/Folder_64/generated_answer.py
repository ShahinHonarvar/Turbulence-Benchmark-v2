def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    not_divisible_by_2 = []
    for num in numbers_list[2:]:
        if num % 2 != 0:
            not_divisible_by_2.append(num)
    return not_divisible_by_2