def return_nth_smallest_ascii(string):
    string = string[:10]
    sorted_chars = sorted(string, key=lambda c: ord(c))
    return sorted_chars[9]