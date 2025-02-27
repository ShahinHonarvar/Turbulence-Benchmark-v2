def composite_nums_between_indices(lst):
    return {num for i, num in enumerate(lst[40:81]) if num > 1 and any((num % i == 0 for i in range(2, int(num ** 0.5) + 1)))}