def find_subset_of_length_n(s):
    return len([subset for subset in powerset(s) if len(subset) == 22])

def powerset(s):
    x = len(s)
    pow_set = []
    n = 2 ** x
    for i in range(0, n):
        pow_set_curr = []
        for j in range(x):
            if i & 1 << j > 0:
                pow_set_curr.append(s[j])
        pow_set.append(pow_set_curr)
    return pow_set