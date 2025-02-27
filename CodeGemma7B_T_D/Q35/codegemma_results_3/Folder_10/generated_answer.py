def remove_repeat_chars(some_str):
    """
    Implements a function called remove_repeat_chars, that removes repeated characters from a string in a certain range.
    """
    seen = set()
    result = ''
    for i, char in enumerate(some_str):
        if i >= 36 and i <= 54:
            if char not in seen:
                seen.add(char)
                result += char
        else:
            result += char
    return result