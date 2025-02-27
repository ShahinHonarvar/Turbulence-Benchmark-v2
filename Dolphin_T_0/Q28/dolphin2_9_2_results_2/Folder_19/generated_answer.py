def return_nth_smallest_ascii(s):
    substring = s[0:18]
    sorted_characters = sorted(substring, key=lambda x: ord(x))
    return sorted_characters[12]