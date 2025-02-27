def composite_nums_between_indices(lst):
    comp_nums = set()
    for num in lst[262:747]:
        if all((num % i != 0 for i in range(2, num))):
            comp_nums.add(num)
    return comp_nums