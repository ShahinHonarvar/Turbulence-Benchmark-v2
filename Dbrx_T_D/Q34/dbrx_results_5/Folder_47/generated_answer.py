def find_original_set(*args):
    if len(args) != 77:
        raise ValueError('Function requires exactly 77 arguments')
    if len(setunion(args)) != 77:
        raise ValueError('Arguments must be distinct')
    all_numbers = {num for arg in args for num in arg}
    return {num for num in all_numbers if all({num in s for s in args})}