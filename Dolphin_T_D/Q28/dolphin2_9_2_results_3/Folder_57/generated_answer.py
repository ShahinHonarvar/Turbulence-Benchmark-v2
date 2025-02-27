def return_nth_smallest_ascii(s):
    substring = s[17:35]
    list_of_chars = list(substring)
    list_of_chars.sort(key=lambda x: ord(x))
    return list_of_chars[17]