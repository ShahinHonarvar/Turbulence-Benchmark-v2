def find_subset_of_length_n(input_set, n):
    if n != 35:
        raise ValueError('Function only supports subset size of 35')
    if not isinstance(input_set, set):
        raise TypeError('Input must be a set')
    if len(input_set) < 35:
        return 0
    subset_count = 0
    for x in input_set:
        for y in input_set.difference({x}):
            for z in input_set.difference({x, y}):
                subset_count += 1
                break
    return subset_count