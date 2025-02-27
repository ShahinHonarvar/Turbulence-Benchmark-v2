def return_nth_smallest_ascii(s):
    substrings = s[5:90]
    sorted_characters = sorted(substrings, key=lambda x: ord(x))
    return sorted_characters[12]