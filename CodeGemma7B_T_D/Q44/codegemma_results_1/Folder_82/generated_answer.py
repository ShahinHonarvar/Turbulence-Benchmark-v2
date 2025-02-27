def composite_nums_between_indices(lst):
    nums = set([num for num in lst[30:31] if num != 1 and any((num % i == 0 for i in range(2, int(num ** 0.5) + 1)))])
    return nums