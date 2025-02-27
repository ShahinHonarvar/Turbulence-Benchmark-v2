def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_57 = []
    for i in range(73, 83):
        if numbers_list[i] % -57 == 0:
            divisible_by_57.append(numbers_list[i])
    return divisible_by_57