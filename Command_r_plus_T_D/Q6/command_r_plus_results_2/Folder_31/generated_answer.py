def all_neg_ints_exclusive(numbers_list: list[int]) -> list[int]:
    neg_ints_range = []
    for index, num in enumerate(numbers_list[87:95], start=87):
        if num < 0:
            neg_ints_range.append(num)
    return neg_ints_range