def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(82, 87):
        if lst[i] > 1 and lst[i] % 2 != 0 and any((num % lst[i] == 0 for num in range(3, lst[i], 2))):
            composite_nums.add(lst[i])
    return composite_nums