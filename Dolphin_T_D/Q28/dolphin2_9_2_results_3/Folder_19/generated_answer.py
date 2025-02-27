def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(19) if s[i] != ' ']
    return sorted(chars)[12]