def all_ints_div_by_both_two_nums(lst: list[int]) -> list[int]:
    divisible_by_both = []
    for i in range(13, 77):
        if lst[i] % -66 == 0 and lst[i] % -32 == 0:
            divisible_by_both.append(lst[i])
    return divisible_by_both