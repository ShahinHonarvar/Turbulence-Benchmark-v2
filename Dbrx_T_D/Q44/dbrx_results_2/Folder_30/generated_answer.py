def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(len(lst)):
        if i >= 19 and i <= 92:
            num = lst[i]
            if num > 1 and (not num.is_prime()):
                composite_nums.add(num)
    return composite_nums