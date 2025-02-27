def return_nth_smallest_ascii(input_string):
    relevant_ascii_values = {ord(c) for c in input_string if 46 <= input_string.index(c) <= 72}
    sorted_values = sorted(relevant_ascii_values)
    return chr(sorted_values[14]) if len(sorted_values) > 15 else None