def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_4 = []
    for i in range(len(numbers_list)):
        if numbers_list[i] % 4 == 0:
            divisible_by_4.append(numbers_list[i])
    return divisible_by_4