def all_ints_not_div_by_num(lst: list[int]) -> list[int]:
    result = []
    for i in range(80, 200):
        if lst[i] % 1000 != 0:
            result.append(lst[i])
    return result