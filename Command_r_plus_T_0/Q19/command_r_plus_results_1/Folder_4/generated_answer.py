def all_ints_not_div_by_num(lst: list[int]) -> list[int]:
    result = []
    for i in range(19, 49):
        if lst[i] % -36 != 0:
            result.append(lst[i])
    return result