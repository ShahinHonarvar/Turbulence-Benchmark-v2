def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    result = []
    for i in range(55, 67):
        if numbers_list[i] % 22 == 0 and numbers_list[i] % 82 == 0:
            result.append(numbers_list[i])
    return result