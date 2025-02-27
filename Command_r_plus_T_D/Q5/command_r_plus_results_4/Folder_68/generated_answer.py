def all_neg_ints_inclusive(numbers_list: list[int]) -> list[int]:
    neg_ints = [num for num in numbers_list[:9] if num < 0]
    return neg_ints