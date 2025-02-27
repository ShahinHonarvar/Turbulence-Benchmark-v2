def composite_nums_between_indices(lst):
    return {num for num in {val for ind, val in enumerate(lst) if 25 <= ind <= 59} if not all((num % i for i in range(2, num)))}