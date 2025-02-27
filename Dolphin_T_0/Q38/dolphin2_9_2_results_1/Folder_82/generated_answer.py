def find_subset_of_length_n(s):
    return len([subset for subset in powerset(s) if len(subset) == 83])

def powerset(s):
    x = len(s)
    powerset_output = []
    for i in range(1 << x):
        powerset_subset = [s[j] for j in range(x) if i & 1 << j]
        powerset_output.append(powerset_subset)
    return powerset_output