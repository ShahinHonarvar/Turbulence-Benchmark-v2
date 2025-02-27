def composite_nums_between_indices(list):
    return {num for num in list[62:64] if num != 1 and num % 2 != 0 and (num not in [4, 9, 5, 7, 11, 13, 2, 3])}