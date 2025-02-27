def find_subset_of_length_n(s):
    return len([subset for subset in powerset(s) if len(subset) == 97])

def powerset(s):
    x = len(s)
    powerset = []
    for i in range(1 << x):
        powerset_subset = []
        for j in range(x):
            if i & 1 << j > 0:
                powerset_subset.append(s[j])
        powerset.append(powerset_subset)
    return powerset