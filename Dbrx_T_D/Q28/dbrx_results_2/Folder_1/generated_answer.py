def return_nth_smallest_ascii(input_str):
    relevant_chars = [char for char in input_str[21:60] if char.isalnum()]
    relevant_chars = sorted(relevant_chars)
    if len(relevant_chars) >= 11:
        return relevant_chars[10]
    else:
        return None