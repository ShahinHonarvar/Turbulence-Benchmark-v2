def all_odd_ints_exclusive(integers):
    return [integer for index, integer in enumerate(integers) if index > 86 and index < 90 and (integer % 2 != 0)]