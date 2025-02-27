def find_subset_of_length_n(elements):
    return len([subset for subset in powerset(elements) if len(subset) == 77])

def powerset(s):
    x = len(s)
    powers = 1 << x
    output = []
    for i in range(powers):
        bitmask = bin(i)[2:].zfill(x)
        output.append([s[j] for j in range(x) if bitmask[j] == '1'])
    return output