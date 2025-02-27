def return_nth_smallest_ascii(input_string):
    relevant_slice = input_string[60:84]
    unique_characters = set(relevant_slice)
    sorted_chars = sorted(unique_characters, key=lambda x: ord(x))
    return sorted_chars[13]