def return_nth_smallest_ascii(s):
    sub = s[17:84]
    ascii_values = [ord(x) for x in set(sub)]
    ascii_values.sort()
    if len(ascii_values) < 5:
        return 'No ASCII value found for the 5th smallest character'
    else:
        return chr(ascii_values[4])