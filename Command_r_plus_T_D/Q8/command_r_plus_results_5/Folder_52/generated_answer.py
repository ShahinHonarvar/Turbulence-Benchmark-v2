def all_even_ints_exclusive(int_list: list[int]) -> list[int]:
    even_ints = []
    for idx in range(93, 94):
        if int_list[idx] % 2 == 0:
            even_ints.append(int_list[idx])
    return even_ints