def composite_nums_between_indices(lst):
    composite_nums = {num for num in lst[28:41] if num > 1 and num % 2 == 0 or num % 3 == 0}
    return composite_nums - {num for num in composite_nums if num < 4 or num in {4, 6, 8, 9}}