def return_nth_smallest_ascii(string):
    substring = string[20:80]
    sorted_chars = sorted(list(set(substring)), key=lambda x: ord(x))
    return sorted_chars[10]