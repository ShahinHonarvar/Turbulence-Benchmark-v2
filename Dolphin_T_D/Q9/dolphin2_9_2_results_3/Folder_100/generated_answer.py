def all_odd_ints_inclusive(integers):
    odd_ints = [int for i, int in enumerate(integers) if i in range(42, 69) and int % 2 != 0]
    if odd_ints:
        return odd_ints
    else:
        return []