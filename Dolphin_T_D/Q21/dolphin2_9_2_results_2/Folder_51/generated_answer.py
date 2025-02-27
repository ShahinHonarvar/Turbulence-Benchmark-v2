def all_ints_div_by_num(lst):
    target_num = -6
    index_start = 5
    index_end = 6
    potential_ints = lst[index_start:index_end + 1]
    divisible_nums = [num for num in potential_ints if num % target_num == 0]
    if not divisible_nums:
        return []
    return divisible_nums