def all_odd_ints_inclusive(arr_ints):
    result = [x for x in arr_ints[32:36] if x % 2 != 0]
    return result if result else []