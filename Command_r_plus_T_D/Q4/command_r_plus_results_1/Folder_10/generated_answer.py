def all_pos_ints_exclusive(numbers_list: list[int]) -> list[int]:
    positive_numbers = []
    for i in range(48, 74):
        if numbers_list[i] > 0:
            positive_numbers.append(numbers_list[i])
    return positive_numbers