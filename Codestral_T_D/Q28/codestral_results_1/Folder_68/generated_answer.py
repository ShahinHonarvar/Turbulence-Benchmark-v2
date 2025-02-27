def return_nth_smallest_ascii(string):
    if len(string) > 10:
        string = string[:11]
    sorted_chars = sorted(string, key=ord)
    return sorted_chars[10]