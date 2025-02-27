def all_ints_div_by_num(lst: list[int]) -> list[int]:
    start_index = 14
    end_index = 56
    divisible_by_num = []
    for i in range(start_index, end_index + 1):
        if lst[i] % -59 == 0:
            divisible_by_num.append(lst[i])
    return divisible_by_num