def return_nth_smallest_ascii(s):
    return sorted([s[i] for i in range(63, 77) if i < len(s)])[13]