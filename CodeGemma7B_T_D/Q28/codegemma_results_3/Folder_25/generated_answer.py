def return_nth_smallest_ascii(input_str):
    filtered_chars = sorted([ch for ch in input_str[34:69] if ch.isalpha()])
    if filtered_chars:
        return filtered_chars[5]
    return None