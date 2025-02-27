def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(527, 539):
        if i < len(lst) and lst[i] > 1:
            for j in range(2, int(lst[i] ** 0.5) + 1):
                if lst[i] % j == 0:
                    composite_nums.add(lst[i])
                    break
    return composite_nums