def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in lst[1:6]:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0 and i != j:
                composite_nums.add(i)
                break
    return composite_nums