def all_odd_ints_inclusive(ints):
    odd_ints = [int for int in ints[527:539] if int % 2 != 0]
    if not odd_ints:
        return []
    else:
        return odd_ints