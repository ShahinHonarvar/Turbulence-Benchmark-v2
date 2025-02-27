def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    non_divisible_nums = []
    for i in range(70, 200):
        if numbers_list[i] % -300 != 0:
            non_divisible_nums.append(numbers_list[i])
    return non_divisible_nums