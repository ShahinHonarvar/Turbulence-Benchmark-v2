def composite_nums_between_indices(lst):
    if len(lst) < 47:
        return set()
    composite_nums = set()
    for num in lst[36:47]:
        if num > 1 and (not num & 1) and (num % 3 != 0) or num % 5 == 0:
            composite_nums.add(num)
    return composite_nums