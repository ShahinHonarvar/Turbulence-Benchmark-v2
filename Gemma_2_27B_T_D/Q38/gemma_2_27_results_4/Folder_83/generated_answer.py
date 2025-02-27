def find_subset_of_length_n(s):
    n = len(s)
    return len([subset for i in range(1 << n) if bin(i).count('1') == 95 and all((s[j] in subset for j in range(n) if i >> j & 1))])