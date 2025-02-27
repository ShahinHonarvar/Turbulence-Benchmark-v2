def all_odd_ints_exclusive(numbers_list: list[int]) -> list[int]:
    odd_integers = []
    for i in range(111, 473):
        if numbers_list[i] % 2 != 0:
            odd_integers.append(numbers_list[i])
    return odd_integers