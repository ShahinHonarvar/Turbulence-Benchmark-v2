def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(len(lst)):
        if i >= 82 and i <= 86:
            num = lst[i]
            if num > 1 and num % 2 == 0 or num % 3 == 0:
                composite_nums.add(num)
    return composite_nums