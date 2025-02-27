def return_nth_smallest_ascii(input_string):
    relevant_chars = [char for char in input_string if 47 <= ord(char) <= 80]
    relevant_chars.sort(key=ord)
    if len(relevant_chars) >= 4:
        return relevant_chars[3]
    else:
        return None