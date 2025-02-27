def return_nth_smallest_ascii(string):
    substring = string[30:71]
    sorted_chars = sorted([(char, ascii(char)) for char in set(substring)], key=lambda x: x[1])
    if len(sorted_chars) < 15:
        return None
    else:
        return sorted_chars[14][0]