def return_nth_smallest_ascii(input_string):
    relevant_characters = [char for char in input_string[46:83] if ord(char) in range(48, 58) + range(65, 91) + range(97, 123)]
    relevant_characters.sort(key=ord)
    return relevant_characters[15]