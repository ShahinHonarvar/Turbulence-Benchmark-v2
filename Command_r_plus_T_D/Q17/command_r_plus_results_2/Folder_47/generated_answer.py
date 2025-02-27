def all_ints_div_by_both_two_nums(lst: list[int]) -> list[int]:
    if not lst:
        return []
    divisible_by_both = []
    for i in range(42, 88):
        if lst[i] % -90 == 0 and lst[i] % -74 == 0:
            divisible_by_both.append(lst[i])
    return divisible_by_both