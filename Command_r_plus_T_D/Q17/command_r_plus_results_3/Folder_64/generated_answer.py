def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    result = []
    for num in numbers_list[:4]:
        if num % 11 == 0 and num % -7 == 0:
            result.append(num)
    return result