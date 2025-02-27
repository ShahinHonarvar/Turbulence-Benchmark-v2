def return_nth_smallest_ascii(s):
    ascii_vals = [ord(s[i]) for i in range(13)]
    return chr(sorted(ascii_vals)[12])