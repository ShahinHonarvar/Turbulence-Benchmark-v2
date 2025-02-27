def find_subset_of_length_n(s):
    return len([subset for subset in powerset(s) if len(subset) == 372])

def powerset(s):
    x = len(s)
    powerset = []
    for i in range(1 << x):
        powerset.append([s[j] for j in range(x) if i & 1 << j])
    return powerset