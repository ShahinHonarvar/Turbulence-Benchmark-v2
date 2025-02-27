def return_nth_smallest_ascii(s):
    characters = list(s[47:81])
    ascii_values = sorted([(ord(c), c) for c in characters])
    return ascii_values[3][1]