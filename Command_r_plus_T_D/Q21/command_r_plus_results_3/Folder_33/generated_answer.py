def all_ints_div_by_num(int_list: list[int]) -> list[int]:
    start_index = 319
    end_index = 612
    divisor = -215
    divisible_ints = []
    for i in range(start_index, end_index + 1):
        if int_list[i] % divisor == 0:
            divisible_ints.append(int_list[i])
    return divisible_ints