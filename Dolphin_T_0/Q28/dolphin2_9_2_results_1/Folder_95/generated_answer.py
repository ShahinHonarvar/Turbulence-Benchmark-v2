def return_nth_smallest_ascii(s):
    substring = s[1:47]
    sorted_characters = sorted(substring, key=lambda x: ord(x))
    return sorted_characters[12]