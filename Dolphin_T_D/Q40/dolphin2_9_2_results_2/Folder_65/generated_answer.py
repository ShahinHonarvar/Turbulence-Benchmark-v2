def return_n_smallest_chars(s):
    ascii_vals = sorted([s[i] for i in range(len(s))], key=lambda x: ord(x))
    return sorted(ascii_vals[:27], reverse=True)