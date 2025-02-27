def return_nth_smallest_ascii(s):
    return sorted([s[i] for i in range(29, 34) if i < len(s)])[:5][-1]