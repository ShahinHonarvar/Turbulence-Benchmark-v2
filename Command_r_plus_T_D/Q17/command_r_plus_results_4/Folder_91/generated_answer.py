def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    result = []
    for i in range(5):
        if numbers_list[i] % 8 == 0 and numbers_list[i] % -3 == 0:
            result.append(numbers_list[i])
    return result