def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    result = []
    for i in range(73, 87):
        if numbers_list[i] % 54 == 0 and numbers_list[i] % 82 == 0:
            result.append(numbers_list[i])
    return result