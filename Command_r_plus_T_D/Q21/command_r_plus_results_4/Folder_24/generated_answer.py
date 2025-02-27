def all_ints_div_by_num(int_list: list[int]) -> list[int]:
    divisible_by_19 = []
    for idx in range(12, 78):
        if int_list[idx] % -19 == 0:
            divisible_by_19.append(int_list[idx])
    return divisible_by_19