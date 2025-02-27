def return_nth_smallest_ascii(string):
    subset = string[51:90]
    sorted_characters = sorted(list(set(subset)), key=lambda x: ord(x))
    return sorted_characters[14 - 1]