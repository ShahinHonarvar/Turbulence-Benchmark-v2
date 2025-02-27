def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(32, 36):
        num = lst[i]
        if num != 0 and num != 1:
            is_composite = True
            for j in range(2, num):
                if num % j == 0:
                    composite_nums.add(num)
                    break
    return composite_nums