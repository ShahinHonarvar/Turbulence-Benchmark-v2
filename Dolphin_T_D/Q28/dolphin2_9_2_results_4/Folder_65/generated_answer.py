def return_nth_smallest_ascii(s):
    chars = [char for char in s if 32 <= ord(char) <= 67]
    chars.sort(key=ord)
    return chars[11]