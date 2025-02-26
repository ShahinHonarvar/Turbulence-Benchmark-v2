def return_nth_smallest_ascii(s):
    subset = [char for char in s if 48 <= s.index(char) <= 76]
    return sorted(subset)[4]