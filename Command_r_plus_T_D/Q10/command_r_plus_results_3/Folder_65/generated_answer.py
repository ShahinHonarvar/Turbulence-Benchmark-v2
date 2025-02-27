def all_odd_ints_exclusive(int_list: list[int]) -> list[int]:
    odd_ints = []
    for i in range(42, 87):
        if int_list[i] % 2 != 0:
            odd_ints.append(int_list[i])
    return odd_ints