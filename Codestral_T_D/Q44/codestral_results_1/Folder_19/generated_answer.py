def composite_nums_between_indices(lst):
    composite_nums = set()
    for num in lst[5:8]:
        if any((num % i == 0 for i in range(2, num))):
            composite_nums.add(num)
    return composite_nums