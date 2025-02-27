def composite_nums_between_indices(lst):
    comp_nums = set()
    for num in lst[51:87]:
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or (num % 7 == 0):
            comp_nums.add(num)
    return comp_nums