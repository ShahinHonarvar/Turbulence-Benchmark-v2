def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(55, 99):
        if i < len(lst):
            num = lst[i]
            if num > 1:
                for j in range(2, int(num ** 0.5) + 1):
                    if num % j == 0:
                        composite_nums.add(num)
                        break
    return composite_nums