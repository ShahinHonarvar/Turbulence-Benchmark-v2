def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    result = []
    for i in numbers_list[:2]:
        if i % 2 == 0 and i % 1 == 0:
            result.append(i)
    return result