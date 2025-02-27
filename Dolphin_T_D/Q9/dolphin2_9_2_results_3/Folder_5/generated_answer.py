def all_odd_ints_inclusive(x):
    odd_ints = [i for i in x[8:10] if i % 2 != 0]
    if not odd_ints:
        return []
    else:
        return odd_ints