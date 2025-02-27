def return_nth_smallest_ascii(string):
    char_to_ascii = [(char, ord(char)) for char in string]
    filtered_chars = [char for char, ascii in char_to_ascii if 30 <= ascii <= 70]
    filtered_chars.sort(key=ord)
    if filtered_chars:
        return filtered_chars[14]
    return None