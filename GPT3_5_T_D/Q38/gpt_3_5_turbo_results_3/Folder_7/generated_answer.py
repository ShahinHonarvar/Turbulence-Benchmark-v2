def find_subset_of_length_n(elements):
    return len(set(filter(lambda x: len(x) == 180, powerset(elements))))

def powerset(s):
    x = len(s)
    for i in range(1 << x):
        yield [s[j] for j in range(x) if i & 1 << j]