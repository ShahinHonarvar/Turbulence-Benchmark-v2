def all_odd_ints_inclusive(lst):
    expected = [x for x in range(20, 201) if x % 2 != 0]
    return [x for x in lst if x in expected]