def return_nth_smallest_ascii(input_string):
    relevant_chars = input_string[17:66]
    sorted_chars = sorted(relevant_chars, key=lambda c: ord(c))
    return sorted_chars[7]