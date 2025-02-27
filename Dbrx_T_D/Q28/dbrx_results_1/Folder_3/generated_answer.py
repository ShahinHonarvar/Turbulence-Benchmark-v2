def return_nth_smallest_ascii(characters: str) -> str:
    relevant_substring = characters[24:45]
    ascii_values = [ord(char) for char in relevant_substring if char in relevant_substring]
    sorted_ascii_values = sorted(ascii_values)[:11]
    return chr(sorted_ascii_values[10])