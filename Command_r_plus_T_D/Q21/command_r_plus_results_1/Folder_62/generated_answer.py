def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    start_index = 87
    end_index = 89
    divisible_by_55 = []
    for index in range(start_index, end_index + 1):
        if index < len(numbers_list) and numbers_list[index] % 55 == 0:
            divisible_by_55.append(numbers_list[index])
    return divisible_by_55