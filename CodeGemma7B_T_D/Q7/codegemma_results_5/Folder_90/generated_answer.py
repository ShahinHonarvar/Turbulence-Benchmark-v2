def all_even_ints_inclusive(x):
    if not any((i % 2 == 0 for i in x)):
        return []
    return [i for i in x[262:747] if i % 2 == 0]