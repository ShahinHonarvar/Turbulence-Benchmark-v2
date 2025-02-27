def composite_nums_between_indices(list1):
    composite_nums = set()
    for i in range(56, 99):
        if i >= len(list1):
            break
        num = list1[i]
        if num <= 1:
            continue
        is_composite = False
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_composite = True
                break
        if is_composite:
            composite_nums.add(num)
    return composite_nums