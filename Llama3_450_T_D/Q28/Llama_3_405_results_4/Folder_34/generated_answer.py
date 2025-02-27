def return_nth_smallest_ascii(s):
    ascii_chars = [(ord(char), char) for char in s[:19]]
    ascii_chars.sort()
    return ascii_chars[18][1]