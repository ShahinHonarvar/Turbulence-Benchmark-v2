def is_composite(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    if not isinstance(lst, list) or not all((isinstance(i, int) and i > 0 for i in lst)):
        raise ValueError('Input should be a list of positive integers')
    return {num for num in lst[55:99] if is_composite(num)}