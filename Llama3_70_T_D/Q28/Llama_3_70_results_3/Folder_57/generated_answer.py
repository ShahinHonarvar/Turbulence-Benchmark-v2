def return_nth_smallest_ascii(s):
    s = s[17:35]
    ascii_values = sorted([ord(c) for c in s])
    ascii_values = sorted(ascii_values)
    nth_smallest = [s[i] for i in range(len(s)) if ord(s[i]) == ascii_values[17]]
    return nth_smallest[0]