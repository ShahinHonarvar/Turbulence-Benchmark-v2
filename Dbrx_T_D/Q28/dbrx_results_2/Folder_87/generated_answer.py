def return_nth_smallest_ascii(input_string):
    relevant_chars = [char for char in input_string[29:34] if char != ' ' and char.isalnum()]
    relevant_chars.sort(key=lambda char: ord(char))
    return relevant_chars[4]