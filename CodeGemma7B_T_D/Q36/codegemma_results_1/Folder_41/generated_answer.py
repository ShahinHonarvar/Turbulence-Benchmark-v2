def filter_chars(str):
    """Filters characters from a string based on their ASCII values."""
    new_str = ''
    for char in str:
        if char not in [chr(i) for i in range(81, 89)]:
            new_str += char
    return new_str