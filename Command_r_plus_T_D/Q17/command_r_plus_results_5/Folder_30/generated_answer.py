def all_ints_div_by_both_two_nums(lst: list[int]) -> list[int]:
    if not lst:
        raise ValueError('Input list is empty.')
    start_index = 11
    end_index = 76
    divisible_by_both = []
    for i in range(start_index, end_index + 1):
        if i % -81 == 0 and i % -94 == 0:
            divisible_by_both.append(lst[i])
    return divisible_by_both