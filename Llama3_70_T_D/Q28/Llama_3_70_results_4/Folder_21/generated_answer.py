def return_nth_smallest_ascii(s):
    return sorted([s[i] for i in range(8, 66) if i < len(s)])[5]