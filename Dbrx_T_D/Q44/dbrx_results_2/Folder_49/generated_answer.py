def composite_nums_between_indices(lst):
    return {num for num in {x for x in lst[90:201] if x > 1 and (not all((x % y != 0 for y in range(2, int(x ** 0.5) + 1))))} - {2, 3, 5, 7}}