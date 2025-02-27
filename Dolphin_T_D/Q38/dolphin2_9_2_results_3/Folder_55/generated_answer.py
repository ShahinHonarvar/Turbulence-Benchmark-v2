def find_subset_of_length_n(elements):
    return len([subset for subset in powerset(elements) if len(subset) == 21])

def powerset(s):
    x = len(s)
    powerset_output = []
    for i in range(1 << x):
        powerset_output.append([s[j] for j in range(x) if i & 1 << j])
    return powerset_output