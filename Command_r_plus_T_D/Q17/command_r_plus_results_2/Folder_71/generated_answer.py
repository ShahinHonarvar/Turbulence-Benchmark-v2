def all_ints_div_by_both_two_nums(lst: list[int]) -> list[int]:
    divisible_by_both = []
    for i in range(68, 100):
        if lst[i] % -37 == 0 and lst[i] % -26 == 0:
            divisible_by_both.append(lst[i])
    return divisible_by_both