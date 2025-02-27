def composite_nums_between_indices(lst):
    comp_nums = set()
    for i in range(69, 84):
        num = lst[i]
        if num > 1:
            for j in range(2, num):
                if num % j == 0:
                    comp_nums.add(num)
                    break
    return comp_nums