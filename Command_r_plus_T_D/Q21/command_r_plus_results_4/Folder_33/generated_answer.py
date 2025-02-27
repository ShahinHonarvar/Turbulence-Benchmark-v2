def all_ints_div_by_num(int_list: list[int]) -> list[int]:
    divisible_by_215 = []
    for idx in range(319, 613):
        if int_list[idx] % -215 == 0:
            divisible_by_215.append(int_list[idx])
    return divisible_by_215