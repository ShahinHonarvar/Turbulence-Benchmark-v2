def all_pos_ints_exclusive(numbers_list: list[int]) -> list[int]:
    positive_integers = []
    for index in range(369, 983):
        if numbers_list[index] > 0:
            positive_integers.append(numbers_list[index])
    return positive_integers