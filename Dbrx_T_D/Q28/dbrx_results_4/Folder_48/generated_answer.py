def return_nth_smallest_ascii(input_string: str) -> str:
    relevant_chars = input_string[37:60]
    sorted_chars = sorted(set(relevant_chars))
    return sorted_chars[5] if len(sorted_chars) > 5 else None