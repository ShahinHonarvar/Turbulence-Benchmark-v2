def composite_nums_between_indices(n_list):
    composite_set = set()
    if len(n_list) < 200:
        return composite_set
    for i in range(20, 201):
        num = n_list[i]
        if num > 1:
            has_divisor = False
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    has_divisor = True
                    break
            if has_divisor:
                composite_set.add(num)
    return composite_set