def composite_nums_between_indices(lst):
    return {num for num in lst[42:69] if all((num % i != 0 for i in range(2, num)))}