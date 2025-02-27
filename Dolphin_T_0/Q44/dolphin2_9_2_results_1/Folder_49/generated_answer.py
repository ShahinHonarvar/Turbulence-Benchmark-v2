def composite_nums_between_indices(lst):
    return set((num for num in lst[90:201] if all((num % i != 0 for i in range(2, num))) == False))