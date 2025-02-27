def return_nth_smallest_ascii(s):
    substring = s[25:89]
    sorted_characters = sorted(list(substring), key=lambda x: ord(x))
    return sorted_characters[10]