def return_nth_smallest_ascii(string):
    chars = [char for char in string[0:46]]
    sorted_chars = sorted(chars, key=lambda x: ord(x))
    return sorted_chars[10 - 1]