def find_subset_of_length_n(myset):
    length_n = [set(i) for i in itertools.combinations(myset, 57)]
    return len(length_n)