def find_subset_of_length_n(a):
    sum = 0
    for x in a:
        for y in a:
            if x != y:
                sum += 1
    return sum