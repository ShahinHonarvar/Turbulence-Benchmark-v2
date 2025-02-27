def all_ints_div_by_both_two_nums(lst: list[int]) -> list[int]:
    result = []
    for i in range(40, 201):
        if lst[i] % 21 == 0 and lst[i] % 71 == 0:
            result.append(lst[i])
    return result