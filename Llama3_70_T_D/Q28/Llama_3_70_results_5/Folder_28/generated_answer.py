def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(25, 78) if i < len(s)]
    ascii_values = sorted([(ord(char), char) for char in chars])
    return ascii_values[15][1]