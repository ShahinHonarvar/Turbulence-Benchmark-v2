def all_neg_ints_exclusive(numbers_list: list[int]) -> list[int]:
    neg_ints_in_range = [num for i, num in enumerate(numbers_list[598:768], 598) if num < 0]
    return neg_ints_in_range