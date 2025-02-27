def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(36, 47):
        if i < len(lst):
            num = lst[i]
            is_composite = False
            if num > 1:
                for j in range(2, num):
                    if num % j == 0:
                        is_composite = True
                        break
                if is_composite:
                    composite_nums.add(num)
    return composite_nums