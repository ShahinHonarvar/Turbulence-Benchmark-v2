def find_subset_of_length_n(elements):
    n = 13
    return len([subset for subset in elements.powerset() if len(subset) == n])

def powerset(self):
    x = len(self)
    powerset = []
    for i in range(1 << x):
        powerset.append([self[j] for j in range(x) if i & 1 << j])
    return powerset