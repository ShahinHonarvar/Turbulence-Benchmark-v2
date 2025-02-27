def all_ints_div_by_both_two_nums(int_list: list[int]) -> list[int]:
    divisor_1 = -897
    divisor_2 = -556
    start_index = 315
    end_index = 934
    divisible_by_both = []
    for index in range(start_index, end_index + 1):
        if index < len(int_list) and int_list[index] % divisor_1 == 0 and (int_list[index] % divisor_2 == 0):
            divisible_by_both.append(int_list[index])
    return divisible_by_both