def all_ints_not_div_by_num(lst: list[int]) -> list[int]:
    result = []
    for i in range(20, 50):
        if lst[i] % 40 != 0:
            result.append(lst[i])
    return result