def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s if 5 <= s.index(c) <= 89]
    return chr(sorted(ascii_values)[12])