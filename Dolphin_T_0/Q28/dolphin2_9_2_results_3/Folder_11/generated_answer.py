def return_nth_smallest_ascii(string):
    sorted_chars = sorted([ch for ch in string[9:60] if 9 <= string.index(ch) <= 59], key=lambda x: ord(x))
    return sorted_chars[5]