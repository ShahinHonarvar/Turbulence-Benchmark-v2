def composite_nums_between_indices(lst):
    if len(lst) < 87:
        return set()
    composite_nums = set()
    for num in lst[51:87]:
        if num > 1 and (not num & 1) and (num != 2):
            composite_nums.add(num)
        elif num > 1 and all((num % i for i in range(3, int(num ** 0.5) + 1, 2))):
            composite_nums.add(num)
    return composite_nums