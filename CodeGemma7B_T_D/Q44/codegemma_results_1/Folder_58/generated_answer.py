def composite_nums_between_indices(lst):
    composites = set()
    for num in lst[533:606]:
        if num % 2 == 0 or num % 3 == 0 or any((num % i == 0 for i in range(5, int(num ** 0.5) + 1, 6))):
            composites.add(num)
    return composites