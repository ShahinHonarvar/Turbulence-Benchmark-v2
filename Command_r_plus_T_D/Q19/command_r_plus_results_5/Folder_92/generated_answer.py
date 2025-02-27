def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    result = []
    for num in numbers_list[1:]:
        if num % numbers_list[0] != 0:
            result.append(num)
            break
    return result