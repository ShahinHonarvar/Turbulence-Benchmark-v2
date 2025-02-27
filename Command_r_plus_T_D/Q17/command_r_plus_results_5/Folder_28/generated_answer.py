def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    result = []
    for num in numbers_list[34:82]:
        if num % 27 == 0 and num % 57 == 0:
            result.append(num)
    return result