def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_num = []
    for i in range(12, 78):
        if numbers_list[i] % -19 == 0:
            divisible_by_num.append(numbers_list[i])
    return divisible_by_num