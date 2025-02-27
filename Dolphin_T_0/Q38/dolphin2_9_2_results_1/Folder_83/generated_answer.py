def find_subset_of_length_n(s):
    return len([subset for subset in powerset(s) if len(subset) == 95])

def powerset(s):
    res = [[]]
    for elem in s:
        res.extend([subset + [elem] for subset in res])
    return res