def composite_nums_between_indices(list):
    composite_nums = set()
    for i in range(5, 8):
        if not (list[i] % 2 and list[i] % 3 and list[i] % 5 and list[i] % 7):
            composite_nums.add(list[i])
    return composite_nums or set()