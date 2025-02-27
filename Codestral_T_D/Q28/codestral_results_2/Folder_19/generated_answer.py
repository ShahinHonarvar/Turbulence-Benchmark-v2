def return_nth_smallest_ascii(string):
    sorted_chars = sorted(string[:19], key=ord)
    return sorted_chars[12]