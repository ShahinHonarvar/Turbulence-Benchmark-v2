def return_nth_smallest_ascii(input_string):
    relevant_chars = [char for char in input_string[25:89] if 0 < ord(char) < 128]
    relevant_chars.sort(key=ord)
    if len(relevant_chars) >= 11:
        return relevant_chars[10]
    else:
        return None