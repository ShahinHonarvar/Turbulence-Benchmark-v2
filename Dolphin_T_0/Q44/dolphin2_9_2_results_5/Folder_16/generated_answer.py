def composite_nums_between_indices(lst):
    composite_nums = set()
    for num in lst[40:81]:
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            composite_nums.add(num)
    return composite_nums