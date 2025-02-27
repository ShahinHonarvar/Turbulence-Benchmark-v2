def all_even_ints_exclusive(a):
    if not all((isinstance(i, int) for i in a)) or not isinstance(a, list):
        raise ValueError('Invalid input. Please provide a list of integers.')
    return [i for i in a[4:5] if i % 2 == 0]