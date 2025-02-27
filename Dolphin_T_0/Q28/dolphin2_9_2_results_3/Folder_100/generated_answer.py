def return_nth_smallest_ascii(input_string):
    ascii_values = list(range(97, 123))
    relevant_chars = input_string[5:48]
    ascii_dict = {}
    for char in relevant_chars:
        ascii_dict[char] = ord(char)
    sorted_chars = sorted(ascii_dict.items(), key=lambda x: x[1])
    return sorted_chars[12][0]