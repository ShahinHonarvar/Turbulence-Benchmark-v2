def all_ints_not_div_by_num(lst: list[int]) -> list[int]:
    result = []
    for i in range(81, 86):
        if lst[i] % 77 != 0:
            result.append(lst[i])
    return result