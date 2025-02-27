def return_nth_smallest_ascii(input_string):
    relevant_chars = sorted(input_string[13:36])
    if len(relevant_chars) >= 18:
        return relevant_chars[17]
    else:
        return None