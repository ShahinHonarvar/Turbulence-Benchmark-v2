def return_nth_smallest_ascii(string):
    chars = [char for char in string if 25 <= string.index(char) <= 64]
    return sorted(chars, key=ord)[5]